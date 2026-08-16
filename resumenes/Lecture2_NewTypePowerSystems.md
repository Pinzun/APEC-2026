# Lecture 2 — Development and Technical Directions of New-Type Power Systems

**Speaker:** Prof. Zhang Jianhua, North China Electric Power University (NCEPU)  
IET Fellow · Líder del IEC/TC8 "International Microgrid Standard" Working Group  
**Duración grabación:** ~91 min  
**Archivo fuente:** `Lecture2_NewTypePowerSystems/`

---

## 1. Síntesis ejecutiva

El Prof. Zhang Jianhua presenta el marco conceptual y las direcciones tecnológicas del "nuevo sistema de potencia" (新型电力系统) que China está construyendo hacia carbono neutralidad en 2060. La lectura es técnica y exhaustiva: pasa por las características estructurales del sistema chino, los ocho pilares tecnológicos del nuevo sistema, y termina con aplicaciones concretas en microgrids, sistemas DC y gestión de mercado. Es la charla más densa del programa en términos de contenido técnico.

---

## 2. Contexto político-regulatorio chino

**Decisión de 2021:**
En marzo de 2021, la Comisión Central de Asuntos Financieros y Económicos del PCCh instruyó construir "un nuevo sistema de potencia dominado por nuevas energías (ERNC)", con metas de carbon peak antes de 2030 y carbon neutrality antes de 2060.

**Características estructurales de la energía china:**
- El carbón domina y no cambiará a corto plazo (base de la generación).
- La per cápita de recursos energéticos es baja (carbón = 30% del promedio mundial, petróleo = 20%, gas = 22%).
- La energía está distribuida en sentido inverso a los centros de carga: recursos en noroeste/suroeste → carga en este (transmisión de ultra alta tensión UHVDC como solución).

**Meta "70/80/90" para 2060:**
- 70% de consumo energético: electricidad
- 80% de consumo energético: no fósil
- 90% de generación eléctrica: energía limpia

---

## 3. Evolución del sistema de potencia: tres generaciones

| Generación | Período | Característica |
|---|---|---|
| 1ª | Fines s.XIX – 1970s | Desarrollo inicial, fuentes y red básicas |
| 2ª | 1970s – 2000 | Altamente dependiente de fósiles, insostenible |
| 3ª (nuevo sistema) | 2000 – 2050 | Dominado por energías no fósiles |

La transición hacia el nuevo sistema implica que renovables no son solo un complemento: son el *cuerpo principal* del sistema. El carbón pasa de ser la fuente dominante a ser recurso de respaldo y regulación.

---

## 4. Características del nuevo sistema de potencia

El Prof. Zhang identifica cuatro rasgos operacionales distintivos:

1. **Alta proporción de renovables** con variabilidad e intermitencia intensas
2. **Alta proporción de electrónica de potencia** (inversores, convertidores) → pérdida de inercia del sistema
3. **Crecimiento continuo de carga** con mayor exigencia de calidad de suministro
4. **Retiro progresivo de térmicas** convencionales que proveían inercia, reserva y regulación de frecuencia/voltaje

---

## 5. Las ocho direcciones tecnológicas del nuevo sistema

La PPT estructura el contenido alrededor de ocho "fronteras tecnológicas":

### Dirección 1: Generación masiva de ERNC a gran escala
- Bases de energía eólica/solar en desiertos, zonas Gobi y costa offshore
- Integración hidro-eólica-solar en cuencas del Suroeste
- Proyección: capacidad renovable >5.000 GW para 2060

### Dirección 2: Ultra High Voltage (UHV) — Transmisión de ultra alta tensión
- Red UHV DC + AC como columna vertebral del sistema
- Permite transportar energía >3.000 km desde bases del noroeste a centros de carga del este
- China opera la red UHV más extensa del mundo (>30 proyectos ±800 kV DC)

### Dirección 3: Flexibilidad del sistema
- Retrofit de térmicas para deep peak-shaving (hasta 15-20% de carga mínima)
- Hidro como regulador principal
- Almacenamiento a múltiples escalas temporales
- Demand response como recurso de flexibilidad

### Dirección 4: Sistemas de distribución activos
- Red de distribución pasa de pasiva a activa con DER (generación distribuida, EV, baterías)
- Protección adaptativa: los criterios clásicos de cortocircuito ya no aplican con alta penetración de FV distribuida
  - *"El principio de protección ya ha cambiado. Debemos hacer protección rápida y autorecuperación de la red."*
- Virtual Power Plants (VPP) para balancear fuente-carga en distribución
- Reconexión flexible entre subestaciones de distribución/transmisión

### Dirección 5: Microgrids y sistemas DC
- El Prof. Zhang lidera el grupo de trabajo IEC/TC8 de estándares de microgrids
- Las microgrids permiten operación en modo isla durante contingencias → resiliencia local
- Sistemas DC de baja tensión (380 V DC) para alimentar cargas electrónicas sin convertidores AC-DC intermedios
- Integración de: PV + almacenamiento + cargas + EV en un ecosistema DC

**Características del nuevo sistema (fuente-red-carga-almacenamiento):**
- Fuente sigue a la carga (tradicional) → *Carga responde a la oferta* (nuevo paradigma)
- Almacenamiento balancea fluctuaciones
- Operación coordinada inteligente y compatible con la red

### Dirección 6: Control y operación del sistema bajo alta penetración de electrónica de potencia
- Inversores de red con control de inercia virtual (VSM — Virtual Synchronous Machine)
- Los dispositivos de electrónica de potencia actúan en milisegundos → cambios de frecuencia y voltaje mucho más rápidos que antes
- Necesidad de nuevos modelos de estabilidad y esquemas de protección

### Dirección 7: Digitalización e inteligencia
- Big data del sistema de potencia para soporte de operación y planificación
- IA aplicada a: pronóstico renovable, despacho óptimo, mantenimiento predictivo
- Plataformas de datos climáticos y de carbono integradas a la operación

### Dirección 8: Mercado orientado a la optimización de recursos
- Mercado eléctrico multi-nivel (spot + capacidad + servicios auxiliares + carbono)
- Participación plena de ERNC en el mercado
- Exploración de mecanismos de compensación de capacidad y mercados de capacidad
- Alineación entre mercado de carbono, certificados verdes y mercado eléctrico

*"Mejorar los mercados eléctricos multi-nivel. Promover la participación plena de las renovables. Explorar mecanismos de compensación de capacidad y mercados de capacidad. Mejorar el mecanismo de respuesta de la demanda."*

---

## 6. Aplicaciones tecnológicas destacadas

### Microgrid
Definición: sistema de generación, almacenamiento y carga que puede operar conectado o en isla. El Prof. Zhang lidera el estándar IEC sobre microgrids.

**Tipos:**
- Microgrid AC: compatible con la red existente
- Microgrid DC: más eficiente para cargas electrónicas (centros de datos, EV)
- Microgrid híbrida AC/DC

**Beneficios:**
- Mayor penetración renovable
- Menores costos, mayor flexibilidad
- Suministro confiable y sostenible

### Plataforma de big data para el sistema de potencia
- Integra datos meteorológicos, de operación SCADA, de mercado y de emisiones
- Permite pronosticar output renovable, detectar anomalías, optimizar despacho
- Proyecto piloto en Guangxi: plataforma regional de big data para soporte del nuevo sistema de potencia

---

## 7. Datos y cifras clave

| Indicador | Valor |
|---|---|
| Meta carbón en generación para 2060 (China) | ~300 Mt (vs. 1.700 Mt actuales) |
| Capacidad total instalada (China, 2025) | ~3.891 GW |
| Capacidad eólica (China, 2025) | ~640 GW |
| Capacidad solar (China, 2025) | ~1.200 GW |
| Biomasa (China, 2025) | ~47 GW |
| Meta generación limpia 2060 | >90% |

---

## 8. Preguntas y discusión (Q&A)

La sesión incluyó preguntas técnicas al cierre. El Prof. Zhang fue presentado formalmente al inicio ("Please welcome Professor Zhang Nianhua") y al cierre se le agradeció explícitamente ("Thank you Professor Zhang Guoyang for your exciting lecture").

---

## 9. Relevancia para Chile

**Paradigma fuente-red-carga-almacenamiento:**
Chile está en transición hacia este paradigma. La Alta penetración de solar en el norte y eólico en el sur genera desbalances regionales que requieren exactamente el tipo de coordinación que China está desarrollando: transmisión de largo alcance (troncal norte-sur), almacenamiento a múltiples escalas y demand response.

**Microgrids en zonas aisladas:**
Chile tiene sistemas aislados (Aysén, Magallanes) que son candidatos naturales para microgrids renovables con almacenamiento. La experiencia china y los estándares IEC liderados por Zhang son directamente aplicables.

**Pérdida de inercia:**
Con alta penetración fotovoltaica y eólica (ambos via inversores), Chile enfrenta el mismo problema de pérdida de inercia que China. Los inversores de inercia virtual (VSM) son una solución técnica relevante para el CNE/Coordinador.

**Mercado multi-nivel:**
La Dirección 8 es directamente relevante para Chile: el diseño de un mecanismo de capacidad, la integración del carbono con el mercado eléctrico y la alineación con certificados de energía renovable son preguntas abiertas en la regulación chilena.

**Deep peak-shaving de térmicas:**
Las termoeléctricas de carbón en Chile (zona central-sur) podrían hacer el mismo retrofit de flexibilidad que China está completando a escala masiva, extendiendo su vida útil como recursos de regulación antes del cierre definitivo.
