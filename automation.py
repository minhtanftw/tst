import time
import datetime
import subprocess


def check_service_status():
    print(f"[{datetime.datetime.now()}] Checkin service status, ..")
    #simulate a test(you could call pytest, ping, etc,...)
    result = subprocess.run(["ping", "-n","1", "google.com"], capture_output= True, text= True)

    if result.returncode == 0:
        print(" Internet connection OK")
    else:
        print("Connection failed")

def continuous_runner(interval = 60):
    while True:
        check_service_status()
        time.sleep(interval)

if __name__ == "__main__":
    continuous_runner(interval=300)