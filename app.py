import os
import sqlite3
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


BASE = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE, 'test.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_PATH
db = SQLAlchemy(app)

import models


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/data')
def data():
    all_data = []
    query = models.Currency.query.all()
    for row in query:
        obj = {
            'exchange': row.exchange,
            'price': row.price,
            'time': row.horah
        }
        all_data.append(obj)
    return jsonify(all_data)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
