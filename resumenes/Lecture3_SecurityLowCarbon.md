# Lecture 3 — New Power System Security and Low-Carbon Transformation

**Speaker:** Prof. Zhang Jianhua, North China Electric Power University (NCEPU)  
**Duración grabación:** ~156 min total (parte 1: ~84 min + parte 2: ~71 min)  
**Archivos fuente:** `Lecture3_SecurityLowCarbon_parte1/` + `Lecture3_SecurityLowCarbon_parte2/`  
**Nota:** Continuación directa de la Lecture 2 (mismo ponente, misma jornada)

---

## 1. Síntesis ejecutiva

Esta es la sesión técnica más densa del programa, en dos bloques. El Prof. Zhang aborda los dos grandes desafíos de seguridad del nuevo sistema de potencia: (1) seguridad operacional bajo alta penetración de energía electrónica y renovables, y (2) la transformación low-carbon mediante la coordinación fuente-red-carga-almacenamiento con los nuevos factores de clima (气, qì) y carbono (碳, tàn). La sesión cierra con aplicaciones concretas: VPP, protección adaptativa, robots de operación en tensión, plataformas de big data y coordinación con el mercado de carbono.

---

## 2. Parte 1: Seguridad del nuevo sistema de potencia

### 2.1 Nuevas características de operación que generan riesgos

El Prof. Zhang identifica cuatro cambios estructurales que hacen más compleja la seguridad:

1. **Eficiente consumo y operación estable con alta proporción de renovables** → la variabilidad e intermitencia del output son intrínsecas, no eliminables
2. **Masiva integración de dispositivos de electrónica de potencia** → responden en milisegundos/microsegundos, mucho más rápido que las máquinas síncronas convencionales
3. **Crecimiento continuo de la carga con alta exigencia de calidad** → los usuarios industriales y de datos son intolerantes a interrupciones
4. **Retiro progresivo de térmicas convencionales** → se pierde inercia, soporte de voltaje reactivo y capacidad de cortocircuito que antes estabilizaban el sistema

**Consecuencias técnicas:**
- La estructura del sistema se vuelve más compleja; la capacidad de balancear fluctuaciones de renovables desde el ángulo sistémico se debilita
- La pérdida de inercia lleva a caídas de frecuencia más rápidas y profundas ante perturbaciones
- Las cargas se vuelven más de "potencia constante" (inversores) → menor autorregulación de voltaje → mayor sensibilidad a perturbaciones de tensión
- La mayor proporción de potencia recibida desde fuera de los centros de carga urbanos reduce el soporte reactivo local

### 2.2 Eventos de blackout como referencia empírica

La PPT documenta grandes apagones recientes como caso de estudio:

| Fecha | País | Causa | Impacto |
|---|---|---|---|
| Mar. 2018 | Brasil | Error de ajuste de protecciones + falla del sistema de control de estabilidad | 21.730 MW; 14 estados |
| Jun. 2019 | Argentina | Rechazo del sistema de control de estabilidad | País casi completo; ~48 M personas; partes de Chile afectadas |
| Ago. 2019 | UK | Cascada: eólico offshore + FV distribuida + gas → caída de frecuencia | ~1 M usuarios |
| Mar. 2022 | Taiwán | Falla en generación → ~8.460 MW perdidos | ~5,49 M usuarios; el peor apagón desde 1999 |
| Jun. 2024 | Hainan (China) | Tifón supertropical | 79 subestaciones 35 kV desconectadas; 836 líneas 10 kV disparadas |

**Lección:** Los apagones modernos son eventos de cascada que combinan fallas técnicas (protecciones, control) con factores meteorológicos y alta penetración de fuentes no síncronas.

### 2.3 Seguridad informática del sistema eléctrico

La digitalización del sistema amplía la superficie de ataque:

- **Ucrania (dic. 2016):** Hackers atacaron el sector eléctrico → apagón de 30 min
- **Colorado, EE.UU. (nov. 2021):** Ransomware a DMEA → disrupción de sistemas de teléfono, email, facturación
- **India (mar. 2018):** Hackeo para robar datos de clientes y extorsión
- **Venezuela (mar. 2019):** Ciberataque → apagones generalizados en 20 estados; algunas áreas sin electricidad por 24 h

*"La IA ha hecho que los ciberataques sean casi automáticos. Un adolescente con IA puede escanear vulnerabilidades del sistema y penetrarlo."*

**Amenazas identificadas:**
- Ataques de hackers / malware / ingeniería social
- Cada etapa del sistema eléctrico (generación, transmisión, transformación, distribución, consumo) es potencialmente vulnerable
- Un ataque exitoso a los sistemas de control puede provocar apagones masivos e irreversibles

### 2.4 Soluciones tecnológicas de seguridad inteligente

La PPT y la transcripción identifican siete líneas de solución:

| Solución | Descripción |
|---|---|
| Ajuste dinámico flexible fuente-almacenamiento-carga | Coordinación en tiempo real para mantener balance |
| Plantas de energía virtuales (VPP) | Agregación de recursos distribuidos para balance fuente-carga |
| Protección rápida y autorecuperación de la red | Protección adaptativa que funciona con inversores en distribución |
| Reconexión flexible entre subestaciones | SOFT OPEN POINTS / flexible interconnection |
| Sistemas de almacenamiento seguros | Con gestión de baterías (BMS) robusto |
| Robots de operación bajo tensión | Mantenimiento de líneas energizadas sin interrupción del servicio |
| Despacho inteligente | Algoritmos de optimización global fuente-red-carga-almacenamiento |

**Nota especial sobre protección adaptativa:**
*"Con alta penetración de FV distribuida conectada al final de las líneas de distribución, las características de cortocircuito han cambiado. El principio de protección ya ha cambiado. Debemos hacer protección rápida."*

Esto es un problema técnico concreto y no trivial: los relés de protección clásicos asumen que la potencia de cortocircuito viene desde la subestación. Con inversores bidireccionales en los extremos, el flujo puede invertirse y la protección existente puede fallar.

---

## 3. Parte 2: Coordinación fuente-red-carga-almacenamiento + Clima + Carbono

### 3.1 El modelo ampliado: 源网荷储气碳 (Fuente-Red-Carga-Almacenamiento-Clima-Carbono)

La Lecture 3 extiende el modelo de la Lecture 2 con dos nuevos elementos:
- **气 (qì) = Clima/Tiempo meteorológico:** el estado del tiempo afecta simultáneamente la producción (renovables) y la demanda (climatización, calefacción), y la disponibilidad de infraestructura
- **碳 (tàn) = Carbono:** la intensidad de carbono de la electricidad es un insumo del mercado de carbono; el valor económico del carbono afecta las decisiones de despacho

*"El clima y el carbono son dos factores muy importantes para el nuevo sistema de potencia en operación, planificación y mantenimiento."*

### 3.2 El clima como factor de operación

**Impactos del tiempo meteorológico extremo:**
- Un tifón puede dejar fuera de servicio decenas de subestaciones simultáneamente (caso Hainan 2024)
- Las ondas de calor aumentan la demanda (air conditioning) y pueden reducir la capacidad de transmisión por calentamiento de conductores
- Las tormentas de nieve afectan líneas de alta tensión en el norte de China

**Incorporación del pronóstico meteorológico a la operación:**
- Modelos NWP (Numerical Weather Prediction) a 15 min - 7 días integrados al EMS
- Alertas tempranas para reforzar seguridad ante eventos extremos
- Planificación de mantenimiento coordinada con ventanas meteorológicas

### 3.3 Carbono como nueva dimensión de la operación

**Contabilidad de carbono del sistema eléctrico:**
- La intensidad de carbono de la electricidad (gCO₂/kWh) varía hora a hora según el mix de generación
- Esta señal de carbono debe integrarse al despacho y a las señales de precio

**Coordinación mercado eléctrico ↔ mercado de carbono:**
*"El carbono generado por la electricidad es muy importante para la neutralidad de carbono del nuevo sistema de potencia. El objetivo final del nuevo sistema de potencia es reducir las emisiones de carbono."*

- Se necesita un mecanismo de transmisión del precio de carbono hacia el mercado eléctrico
- Los mercados de electricidad verde (certificados) deben alinearse con el mercado de carbono chino (ETS)
- China está desarrollando metodologías para rastrear el "flujo de carbono" a través de la red eléctrica

### 3.4 Plataforma de big data para el nuevo sistema de potencia

El Prof. Zhang presenta una plataforma integrada de datos como solución tecnológica habilitadora:

**Capas de la plataforma:**
1. Datos de operación (SCADA, PMU, medidores inteligentes)
2. Datos meteorológicos en tiempo real y pronóstico
3. Datos de mercado (precios spot, posiciones de carbono, contratos)
4. Datos de activos (condición de equipos, mantenimiento)

**Aplicaciones:**
- Soporte a la operación del sistema (análisis de contingencias, plan de despacho)
- Planificación de la red bajo escenarios climáticos
- Contabilidad de carbono en tiempo real
- Mantenimiento predictivo basado en condición

**Proyecto piloto:** Se está implementando esta plataforma en la provincia de Guangxi como caso de demostración.

---

## 4. Datos y cifras clave

| Indicador | Valor |
|---|---|
| Tifón Hainan 2024: subestaciones 35 kV afectadas | 79 |
| Tifón Hainan 2024: líneas 10 kV disparadas | 836 |
| Apagón Argentina 2019: población afectada | ~48 millones |
| Apagón Taiwán 2022: potencia perdida | ~8.460 MW |
| Apagón Taiwán 2022: usuarios afectados | ~5,49 millones |

---

## 5. Preguntas y discusión (Q&A)

La sesión incluyó preguntas al final (no captadas completamente en la grabación de la parte 2). Un participante preguntó sobre el tiempo de implementación de algunos de los sistemas descritos; la respuesta indicó que "el proyecto se configuró el año antepasado y aún no está completo".

---

## 6. Relevancia para Chile

### Gestión de apagones y resiliencia
El blackout de Argentina en junio 2019 afectó partes de Chile. Esto hace que los mecanismos de coordinación binacional y los esquemas de protección ante cascadas sean directamente relevantes. Chile y Argentina están interconectados, y un fallo en el sistema argentino puede propagarse.

### Ciberseguridad del sistema eléctrico
Con la digitalización del Coordinador Eléctrico Nacional y el despliegue de medidores inteligentes, Chile enfrenta el mismo perfil de amenazas que China documenta. La CNE debería considerar marcos de ciberseguridad específicos para infraestructura crítica eléctrica (similar al NERC CIP en EE.UU.).

### Protección en distribución con alta FV
Con la explosiva penetración de generación distribuida FV en Chile (net metering, PPAs de pequeña escala), el problema de la protección adaptativa en distribución es inminente. Los criterios de ajuste de relés deben revisarse ante la bidireccionalidad del flujo.

### Coordinación mercado eléctrico ↔ carbono
Chile tiene un impuesto verde (ley 20.780/20.899) que aplica a generadoras > 50 MW. La posible evolución hacia un mercado de carbono o ETS en Chile haría muy relevante el modelo chino de transmisión del precio de carbono al despacho.

### Big data operacional
El Coordinador Eléctrico Nacional ya opera sistemas de monitoreo avanzado. La integración de pronósticos meteorológicos al EMS (Energy Management System) y la contabilidad de carbono en tiempo real son pasos naturales que los modelos chinos pueden inspirar.

### VPP como recurso de flexibilidad
Chile está explorando el concepto de "prosumidor" y agregación de recursos distribuidos. La experiencia china con VPP como respaldo de seguridad del sistema (no solo arbitraje económico) amplía la visión del rol que pueden jugar estos recursos en el Coordinador.
