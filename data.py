import sqlite3
import requests


def get_data():
    r = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
    return r.json()


def add_data(bitDict):
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        values = ['bitstamp', bitDict['last']]
        c.execute('INSERT INTO currency (exchange, price) VALUES(?, ?)',
                  values)


if __name__ == '__main__':
    data = get_data()
    add_data(data)
