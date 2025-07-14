import pandas as pd
import os

# Leer archivo original
df = pd.read_csv("data/laptops_supermercados.csv")

# Convertir nombres a minúsculas para filtrar mejor
df["nombre"] = df["nombre"].astype(str)
df["nombre_lower"] = df["nombre"].str.lower()

# Palabras que indican que NO es una laptop real
excluir = ["funda", "maletín", "mochila", "accesorio", "soporte", "cooler", "estuche", "adaptador", "base"]

# Eliminar si contienen alguna de esas palabras
df_filtrado = df[~df["nombre_lower"].str.contains('|'.join(excluir))]

# Eliminar columna auxiliar
df_filtrado = df_filtrado.drop(columns=["nombre_lower"])

# Guardar nuevo CSV limpio
os.makedirs("data", exist_ok=True)
df_filtrado.to_csv("data/laptops_limpio.csv", index=False)

print(f"✅ Limpieza completa: {len(df) - len(df_filtrado)} productos eliminados.")
print("📁 Guardado en: data/laptops_limpio.csv")
