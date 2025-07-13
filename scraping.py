import requests
import pandas as pd
import os

# Crear carpeta de salida si no existe
os.makedirs("data", exist_ok=True)

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
            "coin": c["name"],
            "fuente": "CoinGecko",
            "symbol": c["symbol"].upper(),
            "price_usd": c["current_price"],
            "market_cap": c["market_cap"],
            "change_24h": c["price_change_percentage_24h"]
        }
        for c in data
    ]

def fetch_coinlore(top_n=10):
    url = "https://api.coinlore.net/api/tickers/?limit={}".format(top_n)
    r = requests.get(url)
    data = r.json()["data"]
    return [
        {
            "coin": c["name"],
            "fuente": "Coinlore",
            "symbol": c["symbol"].upper(),
            "price_usd": float(c["price_usd"]),
            "market_cap": float(c["market_cap_usd"]),
            "change_24h": float(c["percent_change_24h"])
        }
        for c in data
    ]

def fetch_coinpaprika(top_n=10):
    url = "https://api.coinpaprika.com/v1/tickers"
    r = requests.get(url)
    data = r.json()[:top_n]
    return [
        {
            "coin": c["name"],
            "fuente": "CoinPaprika",
            "symbol": c["symbol"].upper(),
            "price_usd": c["quotes"]["USD"]["price"],
            "market_cap": c["quotes"]["USD"]["market_cap"],
            "change_24h": c["quotes"]["USD"]["percent_change_24h"]
        }
        for c in data
    ]

def main():
    print("🔄 Extrayendo datos de APIs...")

    cg = fetch_coingecko(10)
    cl = fetch_coinlore(10)
    cp = fetch_coinpaprika(10)

    all_data = cg + cl + cp
    df = pd.DataFrame(all_data)
    df.to_csv("data/crypto_por_moneda.csv", index=False)
    print("✅ Datos guardados en 'data/crypto_por_moneda.csv'")

if __name__ == "__main__":
    main()
