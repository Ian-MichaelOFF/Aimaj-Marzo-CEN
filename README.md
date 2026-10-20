# AIMAJ · Calidad del aire en la estación Centro (CEN) · Marzo 2023 vs. 2024

**Sprint 2 · Del dato horario a la evaluación multianual y comparativa histórica**  
Materia: Análisis y visualización de la información 2026B · Universidad de Guadalajara, CUCEI  
Profesora: MC. Nayeli Areli Pérez Padilla  

🔗 **Sitio publicado:** próximamente en Vercel  
📦 **Repositorio:** [GitHub - Análisis Calidad del Aire Estación CEN](https://github.com/Ian-MichaelOFF/Analisis_Calidad_del_aire_estacion_CEN_marzo_2024)  

---

## ¿De qué trata?

**Analistas de Información Meteorológica y Atmosférica de Jalisco (AIMAJ)** es la agencia ficticia del equipo. En este **Sprint 2**, se amplió el proyecto para procesar y contrastar de forma multianual los registros horarios de la estación **Centro (CEN, Guadalajara)** durante **marzo de 2023 y marzo de 2024**.

A partir de los criterios normativos de la **NOM-172-SEMARNAT-2023**, se calculan los indicadores horarios y diarios del **Índice AIRE Y SALUD**, se evalúan correlaciones meteorológicas (temperatura, humedad y viento), se auditan atípicos e inconsistencias estructurales, y se entrega a **SIMAJ** (Sistema de Monitoreo Atmosférico de Jalisco) un tablero interactivo con directrices de alertamiento y toma de decisiones.

---

## Novedades del Sprint 2

1. **Pipeline de Procesamiento Multianual (2023 & 2024):**  
   Se adaptaron los notebooks del Sprint 1 para procesar `CEN_marzo2023.csv` generando:
   - `Datos/CEN_marzo2023_procesado.csv` (744 horas con NowCast de 12 h para partículas, promedio móvil de 8 h para CO e indicadores de la NOM-172).
   - `Datos/numeralia_diaria_2023.csv` (31 días consolidados con el principio de máximo riesgo).
   - `Datos/dashboard_2023.json` y `Datos/dashboard_2024.json`.

2. **Reporte de Atípicos Homologado:**  
   Se generó `Datos/Reporte_Atipicos_CEN_marzo2023.xlsx` con el **mismo formato que el de 2024:
   - Hoja 1: `Valores Atípicos e Inconsistencias` (registro fila por fila de inconsistencias estructurales, valores faltantes y outliers estadísticos según regla 1.5×IQR).
   - Hoja 2: `Resumen` (conteo por tipo de observación).

3. **Módulo de Comparativa Multianual:**  
   - Tarjetas KPI comparativas (días limpios, días de riesgo, exposición promedio y picos máximos).
   - Gráfico de barras comparativo de distribución de categorías Aire y Salud.
   - Frecuencia comparativa por contaminante determinante.
   - Curva de evolución diaria superpuesta (día 1 al 31) con selector dinámico de contaminante.
   - Matriz comparativa día por día con indicador automático de mejora, empeoramiento o sin cambio.

4. **Conmutación Interactiva en Todas las Gráficas:**  
   Cada gráfica y sección del dashboard (Numeralia, Calendario, Simulador, Mes Completo y Disponibilidad) cuenta con sus propios botones de alternancia `[2024]` / `[2023]` sincronizados en tiempo real.

5. **Arquitectura de Datos Externa y Modular:**  
   Se desacoplaron los datos del código fuente HTML; el dashboard carga asíncronamente los archivos desde `Datos/`, manteniendo compatibilidad total tanto en entornos web (`http://`) como en apertura local directa de escritorio (`file://`).

---

## Resultados Principales: Comparativa 2024 vs. 2023

| Indicador clave | Marzo 2024 | Marzo 2023 | Variación / Hallazgo |
| :--- | :---: | :---: | :--- |
| **Horas analizadas** | 744 h (31 días) | 744 h (31 días) | Cobertura temporal completa |
| **Días en categoría Buena** | **11 días** (35%) | 5 días (16%) | **+120%** de días limpios en 2024 |
| **Días en categoría Aceptable** | 17 días (55%) | 16 días (52%) | Nivel de fondo predominante |
| **Días en categoría Mala** | **3 días** (10%) | 9 días (29%) | Reducción notable en 2024 |
| **Días en Muy Mala** | **0 días** (0%) | 1 día (3%) | 2023 registró pico crítico de O₃ (0.136 ppm) |
| **Días de riesgo (Mala + Muy Mala)** | **3 días** (10%) | **10 días** (32%) | **-70%** de días con advertencia sanitaria |
| **PM₂.₅ promedio mensual** | **13.2 µg/m³** | 28.8 µg/m³ | **-54%** en exposición a partículas finas |
| **PM₁₀ promedio mensual** | 40.3 µg/m³ | 42.5 µg/m³ | Concentración estable entre años |
| **Pico horario máximo de O₃** | 0.098 ppm | 0.136 ppm | En 2023 el O₃ rebasó el umbral 'Muy Mala' |
| **Día más crítico del mes** | 28 de marzo | 28 de marzo | Coincidencia temporal de evento agudo |
| **Contaminante dominante** | O₃ (30 días) | O₃ (27 días) | Agente principal en ambos años |

---

## Metodología y Criterios Normativos

El análisis aplica estrictamente la **NOM-172-SEMARNAT-2023** (vigente desde enero de 2024):

1. **Integración Horaria:**
   - **Ozono (O₃):** Concentración horaria directa (1 h).
   - **Monóxido de Carbono (CO):** Promedio móvil de 8 horas (mínimo 6 horas válidas, 75%).
   - **Partículas (PM₁₀ y PM₂.₅):** Indicador NowCast de 12 horas con factor de ponderación exponencial según variabilidad horaria.
2. **Integración Diaria:**
   - **PM₁₀ y PM₂.₅:** Promedio de 24 horas (exige al menos 18 lecturas válidas en el día, 75%).
   - **O₃ y CO:** Valor máximo horario registrado en el día (exige suficiencia de 18 lecturas).
3. **Principio de Máximo Riesgo:** La categoría global del día o la hora corresponde al contaminante que resulte en el nivel de riesgo a la salud más desfavorable.
4. **Tratamiento de Datos y Atípicos:** Se auditó la base con el criterio 1.5×IQR. Los picos matutinos en CO y partículas se conservaron al corresponder a fenómenos físicos reales (inversión térmica y movilidad vehicular matutina).

---

## Componentes del Dashboard

- **Hero con Metadata:** Identificación de la estación y estado de carga de datos.
- **Numeralia Dinámica:** Tarjetas KPI, dona SVG interactiva de categorías y barras de dominancia de contaminantes.
- **Módulo Comparativo 2024 vs 2023:** Métricas de diferencia porcentual, gráficos de categorías pareadas, gráfica de evolución diaria superpuesta con selector y tabla día por día.
- **Calendario Interactivo:** Mapa de calor con colores oficiales de la norma y tabla completa de 31 días ordenable por cualquier columna.
- **Simulador Horario:** Animación hora a hora (0:00 a 23:00) con cielo dinámico día/noche, sol/luna, neblina según PM, rosa de los vientos, tacómetros instantáneos de cada contaminante y bitácora de alertas.
- **Serie Mensual de 744 Horas:** Gráfica continua con scrub interactivo, marcas de horas sin dato y líneas de referencia de norma.
- **Sección Meteorológica:** Análisis de cómo la temperatura y radiación modulan el ozono vespertino, y cómo la inversión térmica y el viento calmo concentran partículas por la mañana.
- **Calculadora NOM-172:** Permite ingresar cualquier concentración y obtener instantáneamente su categoría, color y recomendación de salud.
- **Calidad de Datos:** Disponibilidad de sensores en 2023 vs 2024 y resumen de los reportes de atípicos.
- **Interpretación para SIMAJ:** Respuesta a las preguntas institucionales con distinción explícita entre *hallazgos respaldados por datos* e *interpretaciones sin demostrar*.
- **Catálogo de Alertas:** Matriz de protocolos preventivos y correctivos para la agencia.

---

## Estructura del Proyecto

```
├── index.html                           # Dashboard interactivo completo
├── README.md                            # Documentación del proyecto
├── inspect_2024.py                      # Extractor de métricas y generador de JSON 2024
├── procesar_2023.py                     # Pipeline NOM-172 para marzo 2023
├── generar_reporte_atipicos_2023.py     # Generador del reporte de atípicos 2023 homologado
│
├── Datos/
│   ├── CEN_marzo.xlsx                   # Datos limpios y procesados de marzo 2024
│   ├── CEN_marzo2023.csv                # Datos fuente horarios de marzo 2023
│   ├── CEN_marzo2023.xlsx               # Datos fuente en Excel de marzo 2023
│   ├── CEN_marzo2023_procesado.csv      # Salida horaria con NowCast y CO_8h (2023)
│   ├── numeralia_diaria_2024.csv        # Resumen diario oficial de marzo 2024
│   ├── numeralia_diaria_2023.csv        # Resumen diario oficial de marzo 2023
│   ├── dashboard_2024.json              # Datos compactos para el dashboard (2024)
│   ├── dashboard_2023.json              # Datos compactos para el dashboard (2023)
│   ├── datos_dashboard.js               # Bundle JS de respaldo para ejecución local directa
│   ├── Reporte_Atipicos_CEN_marzo.xlsx  # Auditoría y reporte de atípicos 2024
│   └── Reporte_Atipicos_CEN_marzo2023.xlsx # Auditoría y reporte de atípicos 2023
│
├── Notebooks py/
│   ├── Calculos_Diarios_CEN.ipynb       # Notebook de cálculo de indicadores diarios
│   └── Indice_AIRE_Y_SALUD_CEN (1).ipynb# Notebook de cálculo horario del Índice
│
└── Doc/
    └── 26B_AVI_d04_sp1_eq1_Manzo_Mejía_Susana_Rubi.docx.pdf # Reporte Sprint 1
```

---

## Cómo Ejecutar el Proyecto

1. **Apertura Directa en Local :**
   - Haz doble clic en `index.html` en el Explorador de Windows.
   - El dashboard cargará de inmediato usando los datos de `Datos/datos_dashboard.js` sin requerir servidor web ni configuraciones adicionales.

## Limitaciones Identificadas en los Datos

- **Disponibilidad de PM₂.₅ en 2023:** El sensor de PM₂.₅ presentó interrupciones prolongadas (días 1 al 7 y 18 al 27 sin registros suficientes), acumulando 291 horas faltantes (60.9% disponibilidad frente a 97.2% en 2024). Por norma estricta, no se imputan valores.
- **Variables Meteorológicas en 2024:** En 2024 no se captaron humedad relativa, velocidad de viento ni radiación solar (0% disponibilidad), limitando la correlación en ese periodo a temperatura exterior y dirección de viento. En 2023 sí se dispuso de viento y humedad relativa (68.7% disponibilidad).
- **Representatividad Micro-local:** Los resultados describen específicamente el entorno de la estación Centro (CEN, Sector Libertad) y no deben extrapolarse de forma homogénea a toda el Área Metropolitana de Guadalajara.

---

## Equipo de Trabajo

| Integrante | Rol |
| :--- | :--- |
| **Manzo Mejía Susana Rubí** | Scrum Master |
| **Castellanos Zúñiga Ian Michael** | Storyteller |
| **Montero González José Antonio** | Data Engineer |
| **Melendez González Ángel Leonel** | Data Analyst |
| **Anaya Valladolid Luis Rafael** | Visualization Designer |
| **Magaña Mojica Jesús Ismael** | QA / Documentation |

---

## Uso de IA Generativa

El equipo utilizó herramientas de Inteligencia Artificial Generativa (Gemini y Claude) como soporte para la investigación técnica de lineamientos normativos de la NOM-172-SEMARNAT-2023, la estructuración de la documentación y la optimización de componentes interactivos en JavaScript y CSS. El equipo revisó, auditó y validó la totalidad de los datos, cálculos e interpretaciones técnicas, asumiendo plena responsabilidad del producto final.
