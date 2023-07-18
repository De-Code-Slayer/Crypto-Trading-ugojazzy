import requests
import os

COIN_LAYER_API_KEY = os.getenv('COIN_LAYER_API_KEY')

def get_usd_to_() -> dict:
    exchang_rate = requests.get(f'http://api.coinlayer.com/api/live?access_key={COIN_LAYER_API_KEY}&symbols=BTC,ETH,USDT&target=USD')
    return exchang_rate.json().get('rates')
    
