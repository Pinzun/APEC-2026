# APEC Advanced Training Program — Renewable Energy Transition in Open Electricity Markets
**Fuzhou, China | Agosto 2026**

Repositorio de trabajo personal de Pablo Inzunza (División de Mercados Eléctricos, Ministerio de Energía de Chile). Contiene el pipeline de transcripción de audio, las presentaciones del programa y los resúmenes estructurados de cada lecture.

---

## Resúmenes de lectures

La carpeta [`resumenes/`](resumenes/) es el punto de entrada principal del repositorio.

| # | Lecture | Speaker | Resumen |
|---|---|---|---|
| 1 | Global Energy Markets: Current Landscape and Reform Trends | Dr. Nannan Kou (BloombergNEF) | [→](resumenes/Lecture1_GlobalEnergyMarkets.md) |
| 2 | Development and Technical Directions of New-Type Power Systems | Prof. Zhang Jianhua (NCEPU) | [→](resumenes/Lecture2_NewTypePowerSystems.md) |
| 3 | New Power System Security and Low-Carbon Transformation | Prof. Zhang Jianhua (NCEPU) | [→](resumenes/Lecture3_SecurityLowCarbon.md) |
| 4 | Clean Coal Power Technologies: Status, Development and Practice | — | [→](resumenes/Lecture4_CleanCoalPower.md) |
| 5 | Innovation and Application of New Energy Power Generation Technologies | NCEPU | [→](resumenes/Lecture5_NewEnergyGeneration.md) |
| 6 | Coordination of Energy Storage Deployment and Next-generation Power System Development | Prof. Zechun Hu (Tsinghua) | [→](resumenes/Lecture6_EnergyStorage.md) |
| 7 | Innovative Applications of Digital and Intelligent Technologies in Clean Energy | Jing Teng (NCEPU) | [→](resumenes/Lecture7_DigitalAI_CleanEnergy.md) |

El archivo [`resumenes/00_INDICE.md`](resumenes/00_INDICE.md) incluye el índice completo, los hilos temáticos transversales y una tabla de temas de mayor relevancia para el contexto chileno.

### Actividades de campo
- **Field Study:** Inspección de eólico offshore — Guoneng Shared Platform, Isla Nanri, Putian (plataforma eólico-acuicultura, 4 MW)
- **Visita técnica:** Pingtan Energy Storage Power Station (120 MW / 240 MWh, LFP)
- **Seminar 1:** Which energy storage technologies are expected to see large-scale deployment?
- **Seminar 2:** Which Emerging AI Technologies Could Transform Clean Energy Systems?

---

## Estructura del repositorio

```
APEC-2026/
├── README.md
├── pipeline.py              # Pipeline completo: split → Demucs → Whisper
├── transcribir.py           # Transcripción de un archivo individual
│
├── resumenes/               # ← Punto de entrada principal
│   ├── 00_INDICE.md         # Índice, hilos temáticos y relevancia para Chile
│   ├── Lecture1_GlobalEnergyMarkets.md
│   ├── Lecture2_NewTypePowerSystems.md
│   ├── Lecture3_SecurityLowCarbon.md
│   ├── Lecture4_CleanCoalPower.md
│   ├── Lecture5_NewEnergyGeneration.md
│   ├── Lecture6_EnergyStorage.md
│   └── Lecture7_DigitalAI_CleanEnergy.md
│
└── data/
    ├── raw/                 # ⚠ Excluido de git (.gitignore) — archivos MP4 originales
    ├── ppt/                 # Presentaciones del programa (ZIP con slides + txt extraído)
    └── processed/           # Transcripciones procesadas, una carpeta por grabación
        ├── Lecture1_GlobalEnergyMarkets/
        │   ├── *.json       # Segmentos con timestamps (start, end, text)
        │   ├── *.txt        # Transcripción plana
        │   ├── *.srt        # Subtítulos
        │   └── *_navegable.txt  # Texto con marca de tiempo cada 5 minutos
        ├── Lecture2_NewTypePowerSystems/
        ├── Lecture3_SecurityLowCarbon_parte1/
        ├── Lecture3_SecurityLowCarbon_parte2/
        ├── Lecture4_CleanCoalPower/
        ├── Lecture5_NewEnergyGeneration_parte1/  →  _parte4/
        ├── Lecture6_EnergyStorage_parte1/
        ├── Lecture6_EnergyStorage_parte2/
        ├── Lecture7_DigitalAI_CleanEnergy/
        └── 00_*/            # Sesiones de apertura y contexto institucional
```

---

## Pipeline de transcripción

Las transcripciones se generaron localmente con GPU (RTX 5070 Ti) usando el siguiente stack:

| Herramienta | Rol |
|---|---|
| `ffmpeg` | Segmentación de audio en chunks de ~17 min |
| `Demucs` (`mdx_extra`) | Separación de vocales para mejorar calidad antes de transcribir |
| `faster-whisper` (`large-v3`) | Transcripción en inglés con VAD filter |

### Uso

```bash
# Transcribir todos los archivos nuevos en data/raw/
python pipeline.py

# Transcribir un archivo individual
python transcribir.py data/raw/archivo.mp4
```

**Requisitos:** Python 3.10+, CUDA, `faster-whisper`, `demucs`, `ffmpeg`.

```bash
pip install faster-whisper demucs
```

Cada archivo procesado genera cuatro outputs en `data/processed/<nombre>/`:
- `<nombre>.json` — segmentos con timestamps, formato `[{start, end, text}]`
- `<nombre>.txt` — transcripción plana
- `<nombre>.srt` — subtítulos para reproductores de video
- `<nombre>_navegable.txt` — transcripción con marca de tiempo cada 5 minutos, útil para navegar grabaciones largas

---

## Formato JSON de transcripción

```json
[
  {
    "start": 0.0,
    "end": 5.4,
    "text": "The energy transition is not only about how much we build..."
  },
  ...
]
```

---

## Notas

- Las grabaciones corresponden al 15 de agosto de 2026. Varios audios de una misma lecture se grabaron en partes debido a interrupciones; el match entre archivos y lectures se realizó por análisis de contenido cruzado con las PPT.
- `data/raw/` está excluido de git por tamaño. Las transcripciones procesadas en `data/processed/` sí están versionadas.
- Las PPT originales están en `data/ppt/` en formato ZIP (las distribuyó la organización como archivos compuestos de imágenes + texto extraído por slide).
