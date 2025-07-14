import requests
import pandas as pd
import os

def buscar_en_plazavea(producto, cantidad=10):
    url = "https://www.plazavea.com.pe/api/catalog_system/pub/products/search"
    params = {
        "ft": producto,
        "_from": 0,
        "_to": cantidad - 1
    }
    r = requests.get(url, params=params)
    data = r.json()
    resultados = []
    for item in data:
        try:
            nombre = item['productName']
            precio = item['items'][0]['sellers'][0]['commertialOffer']['Price']
            resultados.append({
                "supermercado": "Plazavea",
                "producto_buscado": producto,
                "nombre": nombre,
                "precio": precio
            })
        except:
            continue
    return resultados

def buscar_en_metro(producto, cantidad=10):
    url = "https://www.metro.pe/api/catalog_system/pub/products/search"
    params = {
        "ft": producto,
        "_from": 0,
        "_to": cantidad - 1
    }
    r = requests.get(url, params=params)
    data = r.json()
    resultados = []
    for item in data:
        try:
            nombre = item['productName']
            precio = item['items'][0]['sellers'][0]['commertialOffer']['Price']
            resultados.append({
                "supermercado": "Metro",
                "producto_buscado": producto,
                "nombre": nombre,
                "precio": precio
            })
        except:
            continue
    return resultados

# Ejecutar búsqueda
productos = ["laptop"]
resultados = []

for prod in productos:
    print(f"🔎 Buscando '{prod}' en Plazavea...")
    resultados.extend(buscar_en_plazavea(prod))

    print(f"🔎 Buscando '{prod}' en Metro...")
    resultados.extend(buscar_en_metro(prod))

# Guardar resultados
df = pd.DataFrame(resultados)
os.makedirs("data", exist_ok=True)
df.to_csv("data/laptops_plazavea_metro.csv", index=False)

print("✅ Archivo generado: data/laptops_plazavea_metro.csv")
df.head()