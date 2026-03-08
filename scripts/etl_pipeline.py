import pandas as pd
import numpy as np
import sqlite3

# 1 cargar datos
df = pd.read_csv("data/raw/compressed_air_leak_raw_dataset.csv")

# 2 limpiar ruido
df = df[df["LeakType"] != "Background Noise"]

# 3 seleccionar columnas importantes
df = df[
[
"LeakID",
"Plant",
"Location",
"Diameter_mm",
"Pressure_psi"
]
]

# 4 calcular perdida de caudal
df["CFM_loss"] = 0.109 * (df["Diameter_mm"]**2) * np.sqrt(df["Pressure_psi"])

# 5 calcular costo anual
cost_per_cfm_hour = 0.25
hours_year = 8000

df["Annual_Cost"] = df["CFM_loss"] * cost_per_cfm_hour * hours_year

# 6 prioridad
df["Priority"] = pd.cut(
df["Annual_Cost"],
bins=[0,10000,100000,500000,1500000],
labels=["Low","Medium","High","Critical",]
)

# 7 ROI meses que tarda en pagarce la reparacion
repair_cost = 500

df["ROI_months"] = repair_cost / (df["Annual_Cost"]/12)

# 8 guardar dataset limpio
df.to_csv("data/processed/leaks_clean.csv", index=False)

# 9 guardar en base de datos
conn = sqlite3.connect("data/energy_audit.db")

df.to_sql("fact_leaks", conn, if_exists="replace", index=False)


print("ETL terminado correctamente")