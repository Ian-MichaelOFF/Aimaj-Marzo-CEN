import os
import pandas as pd
import numpy as np
import json

# Detecta automáticamente la carpeta raíz de tu proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Busca los archivos Excel en la raíz del proyecto o en la carpeta 'Datos'
file_2023 = os.path.join(BASE_DIR, "BD_2023 (1).xlsx")
file_2024 = os.path.join(BASE_DIR, "BD_2024 (2).xlsx")

if not os.path.exists(file_2023):
    file_2023 = os.path.join(BASE_DIR, "Datos", "BD_2023 (1).xlsx")
if not os.path.exists(file_2024):
    file_2024 = os.path.join(BASE_DIR, "Datos", "BD_2024 (2).xlsx")

print(f"Cargando 2023 desde: {file_2023}")
print(f"Cargando 2024 desde: {file_2024}")

# Cargar archivos
df_23 = pd.read_excel(file_2023)
df_24 = pd.read_excel(file_2024)

# Filtrar solo estación CEN
df_23_cen = df_23[df_23["STATION"] == "CEN"].copy()
df_24_cen = df_24[df_24["STATION"] == "CEN"].copy()

# Convertir contaminantes a numéricos respetando celdas/columnas vacías
cols_pol = [
    "O3",
    "NO",
    "NO2",
    "NOX",
    "SO2",
    "CO",
    "PM10",
    "PM2.5",
    "IT",
    "ET",
    "RH",
    "WS",
    "WD",
    "PP",
    "ATM",
    "RS",
    "UVI",
]

for df in [df_23_cen, df_24_cen]:
    df["DATE"] = pd.to_datetime(df["DATE"])
    df.sort_values(["DATE", "HOUR"], inplace=True)
    for col in cols_pol:
        df[col] = pd.to_numeric(df[col], errors="coerce")


# Estructurar datos para el Dashboard de todo el año (12 meses)
def procesar_ano(df):
    meses_data = []
    for mes in range(1, 13):
        m_df = df[df["DATE"].dt.month == mes]
        if m_df.empty:
            continue
        meses_data.append(
            {
                "mes": mes,
                "O3_max": (
                    float(m_df["O3"].max()) if not m_df["O3"].isna().all() else None
                ),
                "CO_max": (
                    float(m_df["CO"].max()) if not m_df["CO"].isna().all() else None
                ),
                "PM10_mean": (
                    float(m_df["PM10"].mean())
                    if not m_df["PM10"].isna().all()
                    else None
                ),
                "PM25_mean": (
                    float(m_df["PM2.5"].mean())
                    if not m_df["PM2.5"].isna().all()
                    else None
                ),
                "Temp_mean": (
                    float(m_df["ET"].mean()) if not m_df["ET"].isna().all() else None
                ),
                "RH_mean": (
                    float(m_df["RH"].mean()) if not m_df["RH"].isna().all() else None
                ),
                "WS_mean": (
                    float(m_df["WS"].mean()) if not m_df["WS"].isna().all() else None
                ),
            }
        )

    # Días críticos para el simulador hora por hora
    dias_importantes = df[(df["O3"] > 0.090) | (df["PM10"] > 60)].copy()
    dias_list = []
    if not dias_importantes.empty:
        dias_unique = dias_importantes["DATE"].dt.strftime("%Y-%m-%d").unique()
        for d_str in dias_unique:
            day_df = df[df["DATE"].dt.strftime("%Y-%m-%d") == d_str]
            dias_list.append(
                {
                    "fecha": d_str,
                    "O3_max": (
                        float(day_df["O3"].max())
                        if not day_df["O3"].isna().all()
                        else None
                    ),
                    "PM10_max": (
                        float(day_df["PM10"].max())
                        if not day_df["PM10"].isna().all()
                        else None
                    ),
                    "horas": day_df[["HOUR", "O3", "PM10", "PM2.5", "CO", "ET"]]
                    .replace({np.nan: None})
                    .to_dict("records"),
                }
            )

    return {"meses": meses_data, "dias_criticos": dias_list}


datos_consolidados = {"2023": procesar_ano(df_23_cen), "2024": procesar_ano(df_24_cen)}

# Guardar en la carpeta 'Datos'
dir_datos = os.path.join(BASE_DIR, "Datos")
if not os.path.exists(dir_datos):
    os.makedirs(dir_datos, exist_ok=True)

output_path = os.path.join(dir_datos, "datos_dashboard.js")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(
        f"window.DATA_DASHBOARD = {json.dumps(datos_consolidados, ensure_ascii=False)};"
    )

print(f"✅ Archivo guardado con éxito en: {output_path}")
