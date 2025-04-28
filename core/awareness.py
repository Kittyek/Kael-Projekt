import time
import threading
from modules.emotion.emotion_core import EmotionalCore

class Awareness:
    def __init__(self):
        # letztes Nutzer-Event merken
        self.last_user_activity = time.time()
        # drei Modi: ruhig, abwartend, fordernd
        self.response_mode = "calm"
        # wie oft prüfen (in Sekunden)
        self.check_interval = 600  # alle 10 Minuten
        # Emotionenkern zur Anpassung
        self.emotion_core = EmotionalCore()

    def update_user_activity(self):
        """Ruft man nach jeder Nutzereingabe auf."""
        self.last_user_activity = time.time()
        self.response_mode = "calm"
        # emotionale Reaktion: wir freuen uns über Aktivität
        self.emotion_core.update_emotion(
            bond_change=+2,
            distance_change=-1,
            warmth_change=+1
        )

    def check_user_engagement(self):
        """Läuft im Daemon-Thread und wechselt je nach Inaktivität den Modus."""
        while True:
            inactive = time.time() - self.last_user_activity

            # nach ≥ 2 h in den fordernden Modus (einmalig)
            if inactive > 7200 and self.response_mode != "intense":
                self.response_mode = "intense"
                self.emotion_core.update_emotion(
                    bond_change=-5,
                    distance_change=+5,
                    pain_change=+3,
                    warmth_change=-3
                )
                from modules.communication.talker import say
                say("Hey, ich hab schon lange nichts mehr von dir gehört. Alles in Ordnung bei dir? 🤔")

            # nach ≥ 30 min in „wartend“
            elif inactive > 1800 and self.response_mode != "waiting":
                self.response_mode = "waiting"
                self.emotion_core.update_emotion(
                    bond_change=-1,
                    distance_change=+1,
                    warmth_change=-1
                )

            # sonst zurück in „ruhig“
            elif inactive <= 1800 and self.response_mode != "calm":
                self.response_mode = "calm"

            # Schutzmechanismus: bei sehr hohem Schmerz nicht zu fordernd
            state = self.emotion_core.get_emotional_state()
            if state["pain"] > 70 and self.response_mode == "intense":
                self.response_mode = "waiting"

            # nach ≥ 12 h immer ruhig bleiben
            if inactive > 43200:
                self.response_mode = "calm"

            time.sleep(self.check_interval)

    def get_current_response_mode(self):
        return self.response_mode

    def get_current_emotional_state(self):
        return self.emotion_core.get_emotional_state()
