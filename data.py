import requests

from app import db
from models import Currency


def get_rates():
    results = {}
    try:
        bitstamp = requests.get(
            'https://www.bitstamp.net/api/v2/ticker/btcusd/')
        results['bitstamp'] = float(bitstamp.json()['bid'])
        kraken = requests.get(
            'https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        results['kraken'] = float(kraken.json()['result']['XXBTZUSD']['a'][0])
        bittrex = requests.get(
            'https://bittrex.com/api/v1.1/public/getticker?market=usdt-btc')
        results['bittrex'] = bittrex.json()['result']['Bid']
        return results
    except:
        return False


def add_data(bitDict):
    for key, value in bitDict.items():
        new_entry = Currency(key, value, None)
        db.session.add(new_entry)
        db.session.commit()


if __name__ == '__main__':
    data = get_rates()
    add_data(data)
