import requests
import pandas as pd
import os

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
            "fuente": "CoinGecko",
            "symbol": c["symbol"].upper(),
            "name":   c["name"],
            "price_usd": c["current_price"],
            "market_cap_usd": c["market_cap"],
            "24h_change_pct": c["price_change_percentage_24h"]
        }
        for c in data
    ]

def main():
    cg = fetch_coingecko(10)
    df = pd.DataFrame(cg)
    df.to_csv("data/crypto_coingecko.csv", index=False)
    print(f"✅ Guardados {len(df)} registros en data/crypto_coingecko.csv")

if __name__ == "__main__":
    main()
