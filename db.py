import sqlite3


def drop_table():
    with sqlite3.connect('test.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS currency;""")
    return True


def create_db():
    with sqlite3.connect('test.db') as connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE currency (
                     exchange text,
                     price REAL,
                     horah DATETIME DEFAULT CURRENT_TIMESTAMP
                 );""")
    return True


if __name__ == '__main__':
    drop_table()
    create_db()
