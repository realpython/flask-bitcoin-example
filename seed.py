import csv

import dateutil.parser

from app import db
from models import Currency


def add_data():
    with open('data.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            new_entry = Currency(row[0], row[1], dateutil.parser.parse(row[2]))
            db.session.add(new_entry)
            db.session.commit()


if __name__ == '__main__':
    add_data()
