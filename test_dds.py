import time
import datetime

def task():
    print("good morning ! task running")

while True:
    now = datetime.datetime.now()
    if now.hour == 13 and now.minute == 50:
        task()
        time.sleep(120)