import requests
import pandas as pd

def scrape_api_dummyjson():
    url = "https://dummyjson.com/products/search?q=laptop"
    resp = requests.get(url)
    data = resp.json()
    items = []

    for product in data["products"]:
        items.append({
            "fuente": "DummyJSON API",
            "titulo": product["title"],
            "precio": product["price"],
            "url": product["thumbnail"]
        })

    return items

def main():
    data = scrape_api_dummyjson()

    if not data:
        print("⚠️ No se extrajó nada de la API.")
        return

    df = pd.DataFrame(data)
    df.to_csv("data/laptops_api.csv", index=False)
    print(f"✅ Guardados {len(df)} registros de la API en data/laptops_api.csv")

if __name__ == "__main__":
    main()
