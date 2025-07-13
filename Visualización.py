import pandas as pd
import matplotlib.pyplot as plt
import os

# Carga del CSV
df = pd.read_csv("data/crypto_por_moneda.csv")

# Crear carpeta si no existe
os.makedirs("capturas", exist_ok=True)

# Pivotear para que cada fuente sea una columna
pivot = df.pivot(index="coin", columns="fuente", values="price_usd")

# Gráfico de barras agrupadas
ax = pivot.plot(kind="bar", figsize=(8, 5))
plt.title("Precios de criptomonedas por fuente")
plt.ylabel("Precio (USD)")
plt.xlabel("Criptomoneda")
plt.xticks(rotation=0)
plt.legend(title="Fuente")
plt.tight_layout()
plt.savefig("capturas/precios_por_moneda_ordenado.png")
plt.show()
