import schedule
import time

from data import get_rates, add_data


def test():
    data = get_rates()
    if data:
        add_data(data)
        print('got data')


schedule.every().hour.do(test)

while True:
    schedule.run_pending()
    time.sleep(1)
