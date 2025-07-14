import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer el archivo generado por el scraping
df = pd.read_csv("laptops_limpio (1).csv")

# Agrupar por supermercado y calcular precio promedio
promedios = df.groupby("supermercado")["precio"].mean().sort_values()

# Crear carpeta para capturas si no existe
os.makedirs("capturas", exist_ok=True)

# Crear gráfico de barras
plt.figure(figsize=(8, 5))
bars = plt.bar(promedios.index, promedios.values, color=["#007ACC", "#FF5733", "#2ECC71"])
plt.title("Precio promedio de laptops por supermercado")
plt.xlabel("Supermercado")
plt.ylabel("Precio promedio (S/)")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.4)

# Mostrar etiquetas encima de cada barra
for bar in bars:
    height = round(bar.get_height(), 2)
    plt.text(bar.get_x() + bar.get_width() / 2, height + 50, f"S/ {height}", ha='center', fontsize=9)

# Guardar el gráfico
plt.tight_layout()
plt.savefig("grafico_comparativo.png")
plt.close()

print("✅ Gráfico guardado en: capturas/grafico_comparativo.png")
