# modules/mood/mood_manager.py

class MoodManager:
    def __init__(self):
        self.current_mood = "neutral"
        self.mood_history = []

    def detect_mood(self, text):
        text = text.lower()
        if any(word in text for word in ["traurig", "verloren", "einsam", "schlecht"]):
            self.current_mood = "traurig"
        elif any(word in text for word in ["wütend", "sauer", "genervt", "hass"]):
            self.current_mood = "wütend"
        elif any(word in text for word in ["glücklich", "freue", "lachen", "gut drauf"]):
            self.current_mood = "glücklich"
        elif any(word in text for word in ["ruhig", "entspannt", "friedlich", "okay"]):
            self.current_mood = "ruhig"
        else:
            self.current_mood = "neutral"

        self.mood_history.append(self.current_mood)
        print(f"[Mood] Stimmung erkannt: {self.current_mood}")

    def get_current_mood(self):
        return self.current_mood

    def show_mood_history(self):
        print("[Mood] Stimmungshistorie:")
        for mood in self.mood_history:
            print(f"- {mood}")
