import os
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/data')
def data():
    all_data = []
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        c.execute("""SELECT * FROM currency""")
        rows = c.fetchall()
        for value in rows:
            all_data.append({
                'exchange': value[0],
                'price': value[1],
                'time': value[1]
            })
        return jsonify(all_data)


if __name__ == '__main__':
    app.run(port=8080)
