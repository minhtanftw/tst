import schedule
import time
import os


def run_test():
    print("RUnning automated test")
    os.system("pytest -v -html = report.html --self-contained-html")

schedule.every().day.at("09:00").do(run_test)
while True:
    schedule.run_pending()
    time.sleep(1)