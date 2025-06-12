from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/price/{coin}")
def get_price(coin: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    return response.json()
