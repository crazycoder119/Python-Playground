import schedule
import requests
import time
from mydata import mobile_number

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hello Chandima Beast time is started  ........ ',
        'key': 'textbelt',
    })
    print(resp.json())


# Every day at 12am or 00:00 time bedtime() is called.
# schedule.every().day.at("6:00").do(send_message)
schedule.every(10).seconds.do(send_message)


while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)