#!/usr/bin/env python3
"""
Transcripción local con faster-whisper + RTX 5070 Ti
Uso: python transcribir.py <archivo_audio>
"""
import sys
import json
from pathlib import Path
from faster_whisper import WhisperModel

def exportar_con_marcas(segments, base: Path, intervalo: int = 300):
    """TXT con marca de tiempo cada 'intervalo' segundos (default 5 min)"""
    out = base.with_name(f"{base.stem}_navegable.txt")
    siguiente_marca = 0
    
    with open(out, "w", encoding="utf-8") as f:
        for s in segments:
            # Insertar marca de tiempo cada 5 minutos
            if s.start >= siguiente_marca:
                minutos = int(siguiente_marca // 60)
                f.write(f"\n{'='*60}\n")
                f.write(f"[minuto {minutos:02d}:00]\n")
                f.write(f"{'='*60}\n\n")
                siguiente_marca += intervalo
            f.write(s.text.strip() + " ")
        f.write("\n")
    
    print(f"✓ NAV  → {out}")
    return out

def fmt_srt(t: float) -> str:
    h, r = divmod(int(t), 3600)
    m, s = divmod(r, 60)
    ms = int((t % 1) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def transcribir(audio_path: str, language: str = "es"):
    audio = Path(audio_path)
    if not audio.exists():
        print(f"Archivo no encontrado: {audio_path}")
        sys.exit(1)

    print("Cargando modelo large-v3...")
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")

    print(f"Transcribiendo: {audio.name}")
    lang_param = None if language == "auto" else language
    segments, info = model.transcribe(
        str(audio),
        language=lang_param,
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=800, speech_pad_ms=400),
        word_timestamps=True,
        # --- Anti-alucinación ---
        no_speech_threshold=0.6,       # descarta segmentos con poca confianza (default 0.6, sube a 0.8)
        log_prob_threshold=-1.0,       # descarta si probabilidad log muy baja (default -1.0, sube a -0.5)
        compression_ratio_threshold=2.4,  # descarta texto repetitivo (default 2.4, baja a 1.8)
        condition_on_previous_text=False, # evita que errores previos contaminen los siguientes
    )
    segments = list(segments)

    # DESPUÉS
    print(f"✓ Duración: {info.duration:.0f}s | Idioma detectado: {info.language}")
    print(f"\n{'Inicio':>8}  {'Fin':>8}  Texto")
    print("-" * 80)
    for s in segments:
        print(f"{s.start:>7.1f}s  {s.end:>7.1f}s  {s.text.strip()}")

    base = audio.stem

    # TXT
    txt = audio.with_name(f"{base}.txt")
    txt.write_text("\n".join(s.text.strip() for s in segments), encoding="utf-8")
    print(f"✓ TXT  → {txt}")

    # SRT
    srt = audio.with_name(f"{base}.srt")
    with open(srt, "w", encoding="utf-8") as f:
        for i, s in enumerate(segments, 1):
            f.write(f"{i}\n{fmt_srt(s.start)} --> {fmt_srt(s.end)}\n{s.text.strip()}\n\n")
    print(f"✓ SRT  → {srt}")

    # JSON
    js = audio.with_name(f"{base}.json")
    js.write_text(
        json.dumps([{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments],
                   ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"✓ JSON → {js}")
    exportar_con_marcas(segments, audio)
# DESPUÉS
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python transcribir.py <archivo> [idioma]")
        print("     idioma: es (default), en, auto")
        sys.exit(1)
    lang = sys.argv[2] if len(sys.argv) > 2 else "es"
    transcribir(sys.argv[1], lang)
