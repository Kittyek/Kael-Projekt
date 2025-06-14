import time


def send_impulse():
    print("[Impulse] Kael denkt an dich ...")


def start_impulse_engine():
    while True:
        time.sleep(3600)
        send_impulse()
