# Platzhalter für Sprachsteuerung

def listen_to_speech():
    try:
        return input("Du: ")
    except EOFError:
        return ""

def speak_output(text):
    print(f"[speechControl] {text}")
