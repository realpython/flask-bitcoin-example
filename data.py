import requests

from app import db
from models import Currency


def get_data():
    r = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
    return r.json()


def add_data(bitDict):
    new_entry = Currency('bitstamp', bitDict['last'], None)
    db.session.add(new_entry)
    db.session.commit()


if __name__ == '__main__':
    data = get_data()
    add_data(data)
