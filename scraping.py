import requests
import pandas as pd
import os

# 1) Prepara carpeta de salida
os.makedirs("data", exist_ok=True)

# 2) Fuente 1: CoinGecko
def fetch_coingecko(top_n=10):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": top_n,
        "page": 1,
        "price_change_percentage": "24h"
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return [
        {
            "fuente": "CoinGecko",
            "symbol": c["symbol"].upper(),
            "name":   c["name"],
            "price_usd": c["current_price"],
            "market_cap_usd": c["market_cap"],
            "change_24h_pct": c["price_change_percentage_24h"]
        }
        for c in data
    ]

# 3) Fuente 2: Coinlore (estable y sin auth)
def fetch_coinlore(top_n=10):
    url = "https://api.coinlore.net/api/tickers/"
    params = {"start": 0, "limit": top_n}
    r = requests.get(url, params=params)
    data = r.json().get("data", [])
    return [
        {
            "fuente": "Coinlore",
            "symbol": c["symbol"],
            "name":   c["name"],
            "price_usd": float(c["price_usd"]),
            "market_cap_usd": float(c["market_cap_usd"]),
            "change_24h_pct": float(c["percent_change_24h"])
        }
        for c in data
    ]

# 4) Fuente 3: CoinPaprika
def fetch_coinpaprika(top_n=10):
    url = "https://api.coinpaprika.com/v1/tickers"
    resp = requests.get(url)
    data = resp.json()[:top_n]
    return [
        {
            "fuente": "CoinPaprika",
            "symbol": c["symbol"].upper(),
            "name":   c["name"],
            "price_usd": c["quotes"]["USD"]["price"],
            "market_cap_usd": c["quotes"]["USD"]["market_cap"],
            "change_24h_pct": c["quotes"]["USD"]["percent_change_24h"]
        }
        for c in data
    ]

# 5) Main: combina y guarda
def main():
    print("🔄 Extrayendo datos de 3 fuentes…")
    cg = fetch_coingecko(10)
    cl = fetch_coinlore(10)
    cp = fetch_coinpaprika(10)

    df = pd.DataFrame(cg + cl + cp)
    df.to_csv("data/crypto_comparativa.csv", index=False)
    print(f"✅ Total registros guardados: {len(df)} en data/crypto_comparativa.csv")

if __name__ == "__main__":
    main()
