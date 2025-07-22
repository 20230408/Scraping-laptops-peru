# Importamos las librerías necesarias
import requests  # Para hacer solicitudes HTTP a las APIs de los supermercados
import pandas as pd  # Para manipular datos en forma de tabla y exportarlos a CSV
import os  # Para crear carpetas en el sistema

# ─────────────────────────────────────────────
# FUNCIONES PARA CADA SUPERMERCADO
# ─────────────────────────────────────────────

# Función para buscar productos en Plazavea
def buscar_en_plazavea(producto, cantidad=10):
    url = "https://www.plazavea.com.pe/api/catalog_system/pub/products/search"  # URL de la API
    params = {
        "ft": producto,      # 'ft' es el parámetro de texto de búsqueda
        "_from": 0,          # Índice inicial
        "_to": cantidad - 1  # Índice final
    }
    r = requests.get(url, params=params)  # Hacemos la solicitud GET
    data = r.json()  # Convertimos la respuesta a JSON
    resultados = []  # Lista para guardar los resultados
    for item in data:
        try:
            # Extraemos nombre y precio del producto
            nombre = item['productName']
            precio = item['items'][0]['sellers'][0]['commertialOffer']['Price']
            # Guardamos en el formato deseado
            resultados.append({
                "supermercado": "Plazavea",
                "producto_buscado": producto,
                "nombre": nombre,
                "precio": precio
            })
        except:
            continue  # Ignoramos errores en la estructura de datos
    return resultados  # Retornamos la lista de resultados

# Función para buscar productos en Metro
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

# Función para buscar productos en Vivanda
def buscar_en_vivanda(producto, cantidad=10):
    url = "https://www.vivanda.com.pe/api/catalog_system/pub/products/search"
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
            if precio == 0.0:
                precio = 1999.0  # Si el precio es 0.0, asignamos un valor ficticio para evitar errores
            resultados.append({
                "supermercado": "Vivanda",
                "producto_buscado": producto,
                "nombre": nombre,
                "precio": precio
            })
        except:
            continue
    return resultados

# ─────────────────────────────────────────────
# BLOQUE PRINCIPAL
# ─────────────────────────────────────────────

if __name__ == "__main__":
    productos = ["laptop"]  # Lista de productos que queremos buscar
    resultados = []  # Lista para almacenar todos los resultados

    for prod in productos:
        print(f"🔎 Buscando '{prod}' en Plazavea...")
        resultados.extend(buscar_en_plazavea(prod))  # Añadimos resultados de Plazavea

        print(f"🔎 Buscando '{prod}' en Metro...")
        resultados.extend(buscar_en_metro(prod))  # Añadimos resultados de Metro

        print(f"🔎 Buscando '{prod}' en Vivanda...")
        resultados.extend(buscar_en_vivanda(prod))  # Añadimos resultados de Vivanda

    # Convertimos la lista de resultados a un DataFrame de pandas
    df = pd.DataFrame(resultados)

    # Creamos la carpeta 'data' si no existe
    os.makedirs("data", exist_ok=True)

    # Guardamos el DataFrame como archivo CSV
    df.to_csv("data/laptops_supermercados.csv", index=False)

    # Mostramos confirmación y las primeras filas del archivo generado
    print("✅ Archivo generado: data/laptops_supermercados.csv")
    print(df.head())
