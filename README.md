# AIMAJ · Calidad del aire en la estación Centro (CEN), marzo 2024

Sprint 1 · **Del dato horario al indicador diario**
Materia: Análisis y visualización de la información 2026B · Universidad de Guadalajara, CUCEI
Profesora: MC. Nayeli Areli Pérez Padilla

🔗 **Sitio publicado:** proximamente en vercel
📦 **Repositorio:** https://github.com/Ian-MichaelOFF/Analisis_Calidad_del_aire_estacion_CEN_marzo_2024

## ¿De qué trata?

Analistas de Información Meteorológica y Atmosférica de Jalisco (AIMAJ) es la agencia ficticia del equipo. Este proyecto presenta a SIMAJ (Sistema de Monitoreo Atmosférico de Jalisco) el análisis de los datos horarios de la estación **CEN (Centro, Guadalajara)** de marzo de 2024. Los convierte en el **Índice AIRE Y SALUD** de la NOM-172-SEMARNAT-2023 y propone alertas y correcciones.

El sitio es un dashboard web (un solo `index.html`, sin dependencias ni proceso de build) con:

- **Numeralia** del mes: categoría predominante, contaminante principal y días críticos.
- **Calendario diario** con categoría y contaminante responsable, y tabla ordenable.
- **Simulador horario:** elige un día y da play para ver, hora por hora, los indicadores, la categoría, la temperatura, el viento y las alertas que se recomendarían.
- **Mes completo:** las 744 horas de marzo con las horas sin dato marcadas.
- **Método:** umbrales de la norma y una calculadora de categorías.
- **Calidad de los datos**, **interpretación de la agencia**, **alertas y correcciones para SIMAJ** y **limitaciones**.

## Resultados principales

| Indicador              | Resultado                             |
| ---------------------- | ------------------------------------- |
| Registros analizados   | 744 horas (31 días × 24 h)            |
| Categoría predominante | Aceptable (16 de 31 días)             |
| Distribución           | 12 días Buena · 16 Aceptable · 3 Mala |
| Contaminante principal | O₃, responsable en 30 días            |
| Días críticos (Mala)   | 10, 12 y 28 de marzo                  |

## Metodología

1. **Revisión del archivo:** sin duplicados, 744 marcas horarias continuas, estación consistente.
2. **Limpieza:** no se eliminó ni imputó ningún valor. Se comparó contra el rango físico de cada variable y se revisaron atípicos con la regla 1.5×IQR.
3. **Cálculo horario:** O₃ con dato horario, CO con promedio móvil de 8 h (mínimo 6 de 8 horas) y PM₁₀ y PM₂.₅ con NowCast de 12 h.
4. **Cálculo diario:** promedio de 24 h para PM₁₀ y PM₂.₅, y máximo del día para O₃ y CO. Se exige un mínimo de 18 lecturas válidas (75 %).
5. **Categoría global:** la del contaminante de mayor riesgo, que se marca como responsable. Los empates cuentan para cada contaminante.

Los umbrales usados son los vigentes desde enero de 2024 según la NOM-172-SEMARNAT-2023.

## Estructura del repositorio

```
├── index.html      # dashboard (lo que publica Vercel)
├── README.md
├── datos/          # CEN_marzo.xlsx y reporte de atípicos
├── notebooks/      # cálculo horario y cálculo diario
└── docs/           # reporte final del Sprint 1 (PDF)
```

## Cómo verlo

- **En línea:** abre el enlace de Vercel.
- **Local:** descarga `index.html` y ábrelo en cualquier navegador. Los datos ya vienen incrustados en el archivo. Solo las tipografías necesitan internet.

## Limitaciones

- La estación **no registró** NO, NO₂, NOₓ, SO₂, humedad relativa, velocidad del viento, precipitación, radiación solar ni índice UV durante todo el mes. Además hay pocos huecos en O₃, CO, PM₁₀ y PM₂.₅.
- Dos bloques de temperatura inusualmente baja (6-7 y 12-13 de marzo) quedaron marcados para revisión y se conservaron. No hay evidencia para decir si fueron un evento real o una falla del sensor.
- Los resultados corresponden **solo al sector de la estación Centro**. No representan a toda la Zona Metropolitana de Guadalajara.

## Datos y fuentes

- Sistema de Monitoreo Atmosférico de Jalisco (SIMAJ), base histórica `BD_2024.xlsx`, estación CEN.
- Secretaría de Medio Ambiente y Recursos Naturales (25 de enero de 2024). _NOM-172-SEMARNAT-2023, Lineamientos para la obtención y comunicación del índice de calidad del aire y riesgos a la salud._ Diario Oficial de la Federación.

## Equipo

| Integrante                     | Rol                    |
| ------------------------------ | ---------------------- |
| Manzo Mejía Susana Rubí        | Scrum Master           |
| Castellanos Zuñiga Ian Michael | Storyteller            |
| Montero González José Antonio  | Data Engineer          |
| Melendez González Ángel Leonel | Data Analyst           |
| Anaya Valladolid Luis Rafael   | Visualization Designer |
| Magaña Mojica Jesús Ismael     | QA / Documentation     |

## Uso de IA generativa

El equipo usó Gemini para investigar conceptos y estructurar el reporte. El dashboard web se desarrolló con ayuda de Claude Code. El equipo revisó y editó el contenido del archivo, y asume la responsabilidad total del trabajo.
