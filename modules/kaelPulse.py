# Dieses Modul sollte separat gestartet werden,
# damit Kael sich bei Inaktivität regelmäßig meldet.

import time


def start_pulse():
    while True:
        print("[kaelPulse] Ping ...")
        time.sleep(300)  # Platzhalter
