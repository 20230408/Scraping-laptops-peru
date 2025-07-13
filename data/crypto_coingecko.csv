import requests
import pandas as pd
import os

# Crear carpeta de salida si no existe
os.makedirs("data", exist_ok=True)

# Fuente 1: CoinGecko (sin clave)
def fetch_coingecko(top_n=10):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": top_n,
        "page": 1,
        "price_change_percentage": "24h"
    }
    r = requests.get(url, params=params)
    data = r.json()
    return [
        {
            "fuente": "CoinGecko",
            "symbol": c["symbol"].upper(),
            "name":   c["name"],
            "price_usd": c["current_price"],
            "market_cap_usd": c["market_cap"],
            "24h_change_pct": c["price_change_percentage_24h"]
        }
        for c in data
    ]

# Fuente 2: CoinCap (sin clave)
def fetch_coincap(top_n=10):
    url = "https://api.coincap.io/v2/assets"
    params = {"limit": top_n}
    r = requests.get(url, params=params)
    data = r.json().get("data", [])
    return [
        {
            "fuente": "CoinCap",
            "symbol": c["symbol"].upper(),
            "name":   c["name"],
            "price_usd": float(c["priceUsd"]),
            "market_cap_usd": float(c["marketCapUsd"]),
            "24h_change_pct": float(c["changePercent24Hr"])
        }
        for c in data
    ]

# Fuente 3: CoinPaprika (sin clave)
def fetch_coinpaprika(top_n=10):
    url = "https://api.coinpaprika.com/v1/tickers"
    r = requests.get(url)
    data = r.json()[:top_n]
    return [
        {
            "fuente": "CoinPaprika",
            "symbol": c["symbol"].upper(),
            "name":   c["name"],
            "price_usd": c["quotes"]["USD"]["price"],
            "market_cap_usd": c["quotes"]["USD"]["market_cap"],
            "24h_change_pct": c["quotes"]["USD"]["percent_change_24h"]
        }
        for c in data
    ]

# Función principal
def main():
    print("🔄 Extrayendo datos...")

    cg = fetch_coingecko(10)
    cc = fetch_coincap(10)
    cp = fetch_coinpaprika(10)

    # Combinar y guardar
    all_data = cg + cc + cp
    df = pd.DataFrame(all_data)
    df.to_csv("data/crypto_comparativa.csv", index=False)
    print(f"✅ Guardados {len(df)} registros en data/crypto_comparativa.csv")

if __name__ == "__main__":
    main()
