import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer los datos
df = pd.read_csv("data/laptops_limpio.csv")

# Ordenar por precio
df = df.sort_values("precio", ascending=False)

# Reducir los nombres para no sobrecargar el eje X
df["nombre_corto"] = df["nombre"].apply(lambda x: x[:40] + "..." if len(x) > 40 else x)

# Crear carpeta para capturas si no existe
os.makedirs("capturas", exist_ok=True)

# Gráfico de barras
plt.figure(figsize=(12, 6))
bars = plt.bar(df["nombre_corto"], df["precio"], color="#4C72B0")
plt.xticks(rotation=90, fontsize=7)
plt.ylabel("Precio (S/)")
plt.title("💻 Precio de cada laptop extraída del scraping")

# Etiquetas encima de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 30, f"S/ {int(yval)}", ha='center', fontsize=6)

plt.tight_layout()
plt.savefig("capturas/precio_laptops_individual.png")
plt.close()

print("✅ Gráfico generado: capturas/precio_laptops_individual.png")
