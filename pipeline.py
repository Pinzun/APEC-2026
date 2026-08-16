#!/usr/bin/env python3
"""
Pipeline: dividir → separar vocales → transcribir
Para todos los archivos de data/raw/ → data/processed/<nombre>/
"""
import sys
import json
import subprocess
from pathlib import Path
from faster_whisper import WhisperModel

# ── Configuración ──────────────────────────────────────────
RAW_DIR       = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
SEGMENT_SECS  = 1050        # ~17 min por chunk para Demucs
LANGUAGE      = "en"
EXTENSIONS    = {".mp4", ".mp3", ".wav", ".m4a", ".flac", ".ogg"}
# ──────────────────────────────────────────────────────────

def run(cmd: list, desc: str = ""):
    print(f"  → {desc or ' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ✗ Error: {result.stderr[-300:]}")
        sys.exit(1)

def fmt_srt(t: float) -> str:
    h, r = divmod(int(t), 3600)
    m, s = divmod(r, 60)
    ms = int((t % 1) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def exportar_navegable(segments, out_dir: Path, base: str, intervalo: int = 300):
    out = out_dir / f"{base}_navegable.txt"
    siguiente_marca = 0
    with open(out, "w", encoding="utf-8") as f:
        for s in segments:
            if s.start >= siguiente_marca:
                minutos = int(siguiente_marca // 60)
                f.write(f"\n{'='*60}\n[minuto {minutos:02d}:00]\n{'='*60}\n\n")
                siguiente_marca += intervalo
            f.write(s.text.strip() + " ")
        f.write("\n")
    print(f"  ✓ NAV  → {out}")

def guardar_outputs(segments, out_dir: Path, base: str, info):
    print(f"  ✓ Duración: {info.duration:.0f}s | Idioma: {info.language}")

    # TXT
    txt = out_dir / f"{base}.txt"
    txt.write_text("\n".join(s.text.strip() for s in segments), encoding="utf-8")
    print(f"  ✓ TXT  → {txt}")

    # SRT
    srt = out_dir / f"{base}.srt"
    with open(srt, "w", encoding="utf-8") as f:
        for i, s in enumerate(segments, 1):
            f.write(f"{i}\n{fmt_srt(s.start)} --> {fmt_srt(s.end)}\n{s.text.strip()}\n\n")
    print(f"  ✓ SRT  → {srt}")

    # JSON
    js = out_dir / f"{base}.json"
    js.write_text(
        json.dumps([{"start": s.start, "end": s.end, "text": s.text.strip()}
                    for s in segments], ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"  ✓ JSON → {js}")

    # Navegable
    exportar_navegable(segments, out_dir, base)

def procesar_audio(audio: Path, model: WhisperModel):
    base = audio.stem
    out_dir = PROCESSED_DIR / base
    out_dir.mkdir(parents=True, exist_ok=True)

    tmp_dir = out_dir / "_tmp"
    tmp_dir.mkdir(exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Procesando: {audio.name}")
    print(f"Output:     {out_dir}")
    print(f"{'='*60}")

    # 1. Dividir en chunks
    print("\n[1/3] Dividiendo en chunks...")
    chunk_pattern = str(tmp_dir / "chunk_%03d.wav")
    run([
        "ffmpeg", "-y", "-i", str(audio),
        "-f", "segment", "-segment_time", str(SEGMENT_SECS),
        "-ar", "44100", "-ac", "2",          # siempre recodificar a WAV estándar
        "-acodec", "pcm_s16le",
        chunk_pattern
    ], "ffmpeg segment")

    chunks = sorted(tmp_dir.glob("chunk_*.wav"))
    print(f"  ✓ {len(chunks)} chunks generados")

    # 2. Separar vocales con Demucs por chunk
    print("\n[2/3] Separando vocales (Demucs)...")
    vocals_list = []
    for chunk in chunks:
        print(f"  Demucs: {chunk.name}")
        run([
            "python", "-m", "demucs",
            "--two-stems=vocals",
            "-n", "mdx_extra",
            "--out", str(tmp_dir / "separated"),
            str(chunk)
        ], f"demucs {chunk.name}")

        vocals_path = tmp_dir / "separated" / "mdx_extra" / chunk.stem / "vocals.wav"
        if not vocals_path.exists():
            print(f"  ✗ No se encontró vocals para {chunk.name}")
            sys.exit(1)
        vocals_list.append(vocals_path)

    # 3. Unir vocals
    print("\n  Uniendo vocals...")
    # Buscar vocals en el orden correcto
    vocals_list = sorted(
        (tmp_dir / "separated" / "mdx_extra").glob("*/vocals.wav"),
        key=lambda p: p.parent.name  # ordena por chunk_000, chunk_001...
    )
    concat_file = tmp_dir / "concat.txt"
    concat_file.write_text(
        "\n".join(f"file '{v.resolve()}'" for v in vocals_list),
        encoding="utf-8"
    )
    vocals_final = tmp_dir / "vocals_final.wav"
    run([
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_file.resolve()),
        "-c", "copy", str(vocals_final.resolve())
    ], "ffmpeg concat vocals")
    print(f"  ✓ vocals_final.wav listo")

    # 4. Transcribir
    print("\n[3/3] Transcribiendo...")
    segments, info = model.transcribe(
        str(vocals_final),
        language=LANGUAGE,
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=800, speech_pad_ms=400),
        word_timestamps=True,
        no_speech_threshold=0.6,
        log_prob_threshold=-1.0,
        compression_ratio_threshold=2.4,
        condition_on_previous_text=False,
    )
    segments = list(segments)
    guardar_outputs(segments, out_dir, base, info)

    # 5. Limpiar temporales
    import shutil
    shutil.rmtree(tmp_dir)
    print(f"  ✓ Temporales eliminados")

def main():
    # Buscar archivos en raw (excluir los que ya tienen carpeta en processed)
    audios = sorted([
        f for f in RAW_DIR.iterdir()
        if f.suffix.lower() in EXTENSIONS
    ])

    if not audios:
        print("No se encontraron archivos en data/raw/")
        sys.exit(0)

    # Filtrar los ya procesados
    pendientes = [
        a for a in audios
        if not (PROCESSED_DIR / a.stem).exists()
    ]

    print(f"Archivos en raw:    {len(audios)}")
    print(f"Ya procesados:      {len(audios) - len(pendientes)}")
    print(f"Pendientes:         {len(pendientes)}")

    if not pendientes:
        print("✓ Todo ya está procesado.")
        sys.exit(0)

    # Cargar modelo una sola vez
    print("\nCargando modelo large-v3...")
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    print("✓ Modelo listo\n")

    for audio in pendientes:
        procesar_audio(audio, model)

    print(f"\n{'='*60}")
    print("✓ Pipeline completado")

if __name__ == "__main__":
    main()
