import urllib.request
import time

def check_internet_connection():
    try:
        urllib.request.urlopen("http://google.com", timeout=3)
        return True
    except:
        return False

def monitor_connection():
    while True:
        connected = check_internet_connection()
        if connected:
            print("🟢 Internetverbindung steht.")
        else:
            print("🔴 Keine Internetverbindung!")
        time.sleep(60)  # jede Minute prüfen
