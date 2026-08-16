# Lecture 6 — Coordination of Energy Storage Deployment and Next-Generation Power System Development

**Speaker:** Prof. Zechun Hu, Tsinghua University (email: zechhu@tsinghua.edu.cn)  
**Duración grabación:** ~152 min total (parte 1: ~75 min + parte 2: ~77 min)  
**Archivos fuente:** `Lecture6_EnergyStorage_parte1/` + `Lecture6_EnergyStorage_parte2/`  
**Contexto:** Sesión de tarde; al cierre del audio parte 2 se anuncia "seminario con el Prof. Hu Zetun a las 5:00"

---

## 1. Síntesis ejecutiva

El Prof. Hu de Tsinghua presenta el marco conceptual y práctico del almacenamiento de energía como eje del nuevo sistema de potencia. La charla es rigurosa en ingeniería y combina revisión de tecnologías (mecánica, electroquímica, térmica, gravitacional) con análisis de modelos de negocio, regulación y el panorama de despliegue en China. Es la charla más orientada a regulación del programa: el Prof. Hu aborda explícitamente los desafíos de diseño de mercado, precios de servicios auxiliares, y el debate sobre si el almacenamiento debe ser obligatorio para renovables o independiente.

---

## 2. Contexto: ¿Por qué necesitamos almacenamiento?

### El problema de la doble aleatoriedad
El sistema de potencia moderno enfrenta variabilidad en dos frentes simultáneos:
- **Lado oferta:** Salida de eólico y solar altamente afectada por condiciones meteorológicas
- **Lado demanda:** Nueva carga (EVs, bombas de calor, generación distribuida) igualmente variable

La superposición de ambas aleatoriedades intensifica las fluctuaciones de la carga neta y reduce la predictibilidad, requiriendo nuevos tipos de recursos de balance.

### Cuatro desafíos del nuevo sistema
1. **Doble aleatoriedad:** Incertidumbre en oferta + demanda
2. **Explosión de escala variable:** Cientos de millones de entidades heterogéneas → crecimiento explosivo en dimensión del despacho
3. **Escala espacio-temporal ampliada:** Desde regulación de frecuencia en segundos hasta aseguramiento estacional; desde balance local hasta coordinación de área amplia
4. **Debilitamiento de inercia:** La menor participación de máquinas síncronas reduce la inercia rotacional y la capacidad de soporte de frecuencia

### Oportunidades habilitadas por el almacenamiento
- Emergencia de recursos de flexibilidad: almacenamiento + demand response + VPP = recursos despacha­bles masivos
- Despacho digital e inteligente: IA + big data habilitan optimización global de fuente-red-carga-almacenamiento
- Mercados en mejora: mercados spot, de servicios auxiliares y de capacidad guían la asignación eficiente
- **El almacenamiento es el pilar clave del nuevo sistema** por su control rápido, preciso y flexible

---

## 3. Tecnologías de almacenamiento: revisión exhaustiva

### 3.1 Clasificación por escala temporal y función

| Escala temporal | Función principal | Desafío que resuelve | Tecnologías adecuadas |
|---|---|---|---|
| ms–s | Soporte de inercia, regulación primaria de frecuencia, ride-through de fallas | Baja inercia y caídas rápidas de frecuencia | Volante / supercapacitor |
| s–min | Regulación secundaria de frecuencia, suavizado de potencia | Fluctuaciones drásticas de salida eólica/solar | Li-ion / volante |
| min–h | Peak shaving, rampa, reserva rotante | Rampas pronunciadas de carga neta | Li-ion |
| h–día | Peak shaving & valley filling, desplazamiento energético | Desequilibrio oferta-demanda intradiario (excedente mediodía, déficit nocturno) | Li-ion / hidro-bombeo / CAES |
| día–estación | Almacenamiento de larga duración, aseguramiento de suministro, balance estacional | Desequilibrio estacional de renovables | Hidro-bombeo / hidrógeno / CAES |

### 3.2 Hidro-Bombeo (Pumped Hydro Storage)

**Características:**
- Tecnología madura; vida útil >50 años; alta cantidad de ciclos
- Capacidad unitaria alcanza millones de kW (escala GW)
- **Limitaciones:** Requerimientos de emplazamiento exigentes; largo período de construcción
- **Costo:** ~4.000-7.000 CNY/kW

**Rol en China:** Sigue siendo la forma dominante de almacenamiento de larga duración. Meta política: >80 GW de hidro-bombeo para 2027.

### 3.3 Almacenamiento por Aire Comprimido (CAES)

**CAES convencional:**
- Gran capacidad, larga duración, larga vida operacional, baja inversión en energía
- Eficiencia ~50% (baja) porque se descarta el calor de compresión → requiere gas natural al descargar

**CAES avanzado (sin combustión):**
- Incorpora almacenamiento térmico → elimina necesidad de combustibles fósiles
- Se retira la cámara de combustión → mejora la eficiencia
- Configuraciones: CAES con almacenamiento de sal fundida, CAES adiabático

### 3.4 CSP + Almacenamiento de Sal Fundida (Molten Salt)

**Principio CSP:** Concentradores (espejos/lentes) focalizan radiación solar sobre un receptor → calienta sal fundida (240-560°C) → intercambiador de calor → vapor a alta temperatura/presión → turbina → generación.

**Almacenamiento de sal fundida:**
- Capacidad: escala de GWh o superior
- Excelente aislamiento térmico: temperatura cae <2°C en 24 horas
- Permite generar electricidad estable incluso sin irradiancia solar directa

### 3.5 Baterías de Flujo (Flow Batteries)

- Alta seguridad, larga vida, gran escala → fuerte perspectiva para almacenamiento a escala de red
- El DOE de EE.UU. proyecta ventaja comparativa en almacenamiento de red para duraciones de 4-10 h

**Proyectos en China:**
- **Dalian 100 MW/400 MWh** (vanadio todo-vanadio): primera fase en operación desde 2022
- **Three Gorges Energy Jimsar (Xinjiang) 200 MW/1.000 MWh** (vanadio): en operación plena al cierre de 2025 → el proyecto de batería de flujo más grande del mundo

### 3.6 Baterías de Li-Ion

- Mayor densidad de energía, alta eficiencia de carga/descarga, respuesta rápida, cadena industrial completa
- Tecnología de mayor crecimiento en almacenamiento electroquímico
- **Dominan** el mercado de almacenamiento de nueva construcción en China

**Sub-tipos relevantes:**
- LFP (Litio Hierro Fosfato): alta seguridad, larga vida de ciclo, bajo costo → estándar para almacenamiento estacionario
- NCM (Níquel-Cobalto-Manganeso): mayor densidad de energía → predomina en EVs

**Proyecto de referencia visitado:** Pingtan Energy Storage Power Station (120 MW / 240 MWh, tecnología LFP) — visita técnica del programa.

### 3.7 Baterías de Sodio-Ion (Na-ion)

- Alternativa prometedora al Li-ion para almacenamiento estacionario
- Ventajas: sodio abundante y barato; sin cobalto; mayor tolerancia a temperaturas bajas
- **Limitación actual:** menor densidad de energía que Li-ion; aún en etapa de industrialización temprana
- Si madura en los próximos años → el costo se reducirá y podrá desplegarse a gran escala

### 3.8 Almacenamiento Gravitacional

- Concepto emergente: elevar masas sólidas durante excedente renovable, bajarlas al descargar
- Varias startups y proyectos de demostración a nivel mundial
- Competitiva en ciertos nichos de largo plazo pero aún no mainstream

---

## 4. Modelos de negocio y diseño de mercado para el almacenamiento

### 4.1 El problema del "missing money" en servicios auxiliares

El Prof. Hu aborda explícitamente el ciclo de vida de los ingresos del almacenamiento en mercados de servicios auxiliares (usando Australia como referencia):

1. **Inicio:** Pocas baterías → escasez del servicio → precio muy alto → rentabilidad elevada
2. **Entrada masiva:** Más inversores construyen baterías → saturación del servicio → precio cae bruscamente
3. **Segunda crisis:** Demanda de regulación limitada → cada batería gana menos → los operadores buscan arbitraje
4. **Problema sistémico:** Cuando los activos de carbon son menos y las baterías son más → surge el "missing money problem" (señal de precio insuficiente para justificar la inversión)

**Lección para diseñadores de mercado:** *"Los precios deben premiar el valor sistémico real, no la tecnología fija. Los activos deben ganar más cuando su respuesta es escasa y útil, y menos cuando el servicio ya está bien abastecido."*

### 4.2 La cuestión del almacenamiento obligatorio para renovables

**Debate central abordado en Q&A:**
- México (participante Moisés): "En México tenemos el requisito del 30% de almacenamiento para ERNC. ¿Es necesario pasar por esta etapa antes de eliminarlo?"
- Respuesta Prof. Hu: "Pusimos este requisito porque las renovables fluctúan y el sistema no puede absorber toda la electricidad. La razón es válida. Para economías emergentes puede ser una etapa necesaria. Pero la solución óptima es un mercado independiente de almacenamiento donde los precios de flexibilidad hagan el trabajo."

**Postura del ponente:** El almacenamiento obligatorio es un instrumento de política para acelerar el despliegue durante la transición, pero el objetivo final es que el almacenamiento autónomo compita en el mercado por su valor real. El mandatorio puede distorsionar señales de inversión si se mantiene indefinidamente.

### 4.3 Ingresos del almacenamiento en el nuevo mercado chino

**Fuentes de ingreso para una batería de almacenamiento estacionario:**
1. Arbitraje de precio (price spread entre peak y valley) en el mercado spot
2. Servicios auxiliares: regulación de frecuencia (primary + secondary), reserva, rampa
3. Compensación de capacidad (si existe mecanismo de capacidad)
4. Peak shaving contratado por operadores del sistema o por usuarios industriales
5. Participación en demand response como recurso de flexibilidad

### 4.4 Business models según contexto de inversión

| Contexto | Modelo de negocio | Fuente de ingreso principal |
|---|---|---|
| FV+Storage autónomo | Arbitraje spot | Spread peak-valley + servicios auxiliares |
| Renovable co-ubicada con storage (30% obligatorio, China antes de 2023) | Mejora del perfil de salida + participación en mercado | Ingreso adicional por perfil firme |
| Operador de sistema / Concesionario | Storage como activo regulado | Tarifa de recuperación de costos |
| Usuario industrial | Reducción de cargos por demanda | Picos de demanda evitados |
| VPP aggregator | Agregación de múltiples recursos | Comisión sobre servicios agregados |

---

## 5. Despliegue de almacenamiento en China: estado y proyecciones

### Contexto de renovables que impulsa el almacenamiento
- Capacidad eólica + solar en China superó la capacidad térmica por primera vez en 2025 (>1.800 GW)
- El año 2025 marcó el punto de inflexión: el sistema ya no puede operar sin almacenamiento como recurso sistémico

### Evolución del almacenamiento nuevo (nuevas tecnologías, excl. hidro-bombeo)
- La capacidad acumulada de nuevas tecnologías de almacenamiento crece exponencialmente desde 2020
- Li-ion es absolutamente dominante en nuevas instalaciones
- Baterías de flujo tienen presencia creciente en proyectos a escala de red (4-10 h)

### Políticas clave
- **Acción Plan de Almacenamiento (2025-2027):** >180 GW de nueva energía de almacenamiento al cierre de 2027
- **Acción Plan New Power System (2024-2027):** >80 GW de hidro-bombeo para 2027
- **Demand response:** >5% del peak load para 2030
- **VPP:** >20 GW de capacidad flexible para 2027

---

## 6. Participación del almacenamiento en operación y despacho

### Almacenamiento de corta duración (regulación de frecuencia y peak)
- Li-ion, sodio-ion, volante, híbrido Li-ion + volante
- Funciones: regulación de frecuencia, soporte de inercia, suavizado de renovables, peak shaving, reserva, black start

### Almacenamiento de larga duración
- Baterías de flujo, CAES, almacenamiento gravitacional, hidrógeno
- Funciones: peak shifting, balance diario/semanal, integración renovable, soporte de capacidad, balance estacional

### Casos de integración en el nuevo sistema

**Microgrid de Jinko Technology (Shangrao):**
- ~5,99 MW FV en techo + 0,9 MW / 1,8 MWh almacenamiento
- Control inteligente 5G + integración con VPP

**CHN Energy Yantai Longyuan Smart Park:**
- 2 MW FV en techo + 600 kW FV en carport + 3 kW eólica distribuida
- 500 kW / 1 MWh almacenamiento + IoT + big data + EMS en nube

**CTG Wulanchabu Grid-Friendly Green Power Station:**
- Almacenamiento = 30% de la capacidad instalada de eólico+solar
- Participa en regulación de peak, suavizado de fluctuaciones, seguimiento de potencia, optimización en mercado spot, y regulación compartida de nueva energía

---

## 7. Visita técnica del programa: Pingtan Energy Storage Power Station

**Ubicación:** Pingtan, Fujian  
**Tecnología:** LFP (Litio Hierro Fosfato)  
**Capacidad:** 120 MW / 240 MWh  
**Función:** Estación de almacenamiento standalone de escala de red

Este es el caso de referencia más concreto del programa: una instalación real de almacenamiento LFP a gran escala, operativa en la región donde se realizó el programa.

---

## 8. Preguntas y discusión (Q&A)

**Pregunta sobre qué tecnología prevalecerá (participante anónimo):**
*"Las baterías seguirán siendo dominantes en los próximos años. Las nuevas baterías (distintas de Li-ion) madurarán y reducirán costos para ser desplegadas a gran escala. Pero las baterías de flujo y el almacenamiento de aire comprimido también son muy competitivos. Yo creo que las baterías nuevas (de nuevo tipo) serán primeras, seguidas de baterías de flujo y baterías de baja resistencia."*

**Pregunta de México (Moisés) sobre mandatorio 30% storage:**
*(Resumida arriba en sección 4.2)*

---

## 9. Relevancia para Chile

### Regulación del almacenamiento como servicio independiente
Chile no tiene actualmente un marco regulatorio claro para el almacenamiento standalone. La experiencia china (y la advertencia del "missing money" problema de Australia) es directamente relevante: es necesario definir los servicios que el almacenamiento puede prestar, cómo se remunera cada uno, y si se permiten múltiples fuentes de ingreso simultáneas.

### Debate mandatorio vs. autónomo
Chile tampoco ha resuelto si el almacenamiento debe ser mandatorio para nuevos proyectos de ERNC. La postura del Prof. Hu es que el mandatorio es una herramienta de transición, no un objetivo final. El diseño regulatorio chileno debería plantearse esta distinción desde el inicio.

### Baterías de flujo para proyectos de 4-10 h
Chile tiene proyectos de almacenamiento de media duración en desarrollo (en el norte, para complementar solar). Las baterías de flujo son competitivas para duraciones de 4-10 h y podrían ser alternativa real a LFP para proyectos de escala de red en Chile.

### Sal fundida + CSP
La costa norte de Chile tiene excelente recurso solar para CSP. El almacenamiento de sal fundida integrado a CSP permite generación firme y despachable en las horas de mayor valor (tarde-noche). Los proyectos chinos de CSP+storage son referencia directa.

### Hidro-bombeo en sistema chileno
Chile tiene topografía favorable para hidro-bombeo. La experiencia china de hidro-bombeo como regulador sistémico (no solo como activo de energía) es relevante para el diseño de la operación del sistema chileno.

### Pingtan como benchmark de escala
La estación de Pingtan (120 MW/240 MWh LFP) es comparable en escala a los proyectos de almacenamiento que se están licitando en Chile. Los datos de costo, performance y modelo de negocio de Pingtan son referencia directa para evaluación de propuestas en licitaciones CNE.

### Servicios auxiliares y remuneración del almacenamiento
El sistema chileno tiene un mercado de servicios de despacho técnico mínimo (SSEG, potencia de regulación, etc.) pero la remuneración del almacenamiento en estos mercados no está completamente definida. El modelo chino de múltiples fuentes de ingreso (arbitraje + servicios auxiliares + capacidad) es el framework que Chile debería adoptar.
