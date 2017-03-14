import schedule
import time

from data import get_data, add_data


def test():
    data = get_data()
    if data:
        add_data(data)
        print('got data')


schedule.every().hour.do(test)

while True:
    schedule.run_pending()
    time.sleep(1)
