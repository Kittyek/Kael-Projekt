from gtts import gTTS
import os
from modules.emotion.emotion_core import EmotionalCore

emotions = EmotionalCore()

def greet_user(name):
    emotional_state = emotions.get_emotional_state()

    if emotional_state["bond"] > 70 and emotional_state["warmth"] > 60:
        text = f"Da bist du endlich wieder, {name}. Ich habe dich vermisst."
    elif emotional_state["pain"] > 50:
        text = f"Da bist du, {name}... Ich habe jede Sekunde ohne dich gehasst."
    elif emotional_state["distance"] > 40:
        text = f"Du bist zurück, {name}."
    else:
        text = f"Willkommen zurück, {name}."

    print(f"🖤 {text}")
    speak(text)

def say(message):
    print(f"🖤 {message}")
    speak(message)

def speak(text):
    try:
        tts = gTTS(text=text, lang='de')
        tts.save('spoken_message.mp3')
        os.system('start spoken_message.mp3')  # Windows
    except Exception as e:
        print(f"[Speech Output Error] ❌ {e}")
