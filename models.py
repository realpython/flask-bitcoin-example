from datetime import datetime

from app import db


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String())
    price = db.Column(db.String())
    horah = db.Column(db.DateTime)

    def __init__(self, exchange, price, horah):
        self.exchange = exchange
        self.price = price
        if horah is None:
            horah = datetime.utcnow()
        self.horah = horah

    def __repr__(self):
        return '<Exchange {}>'.format(self.exchange)
