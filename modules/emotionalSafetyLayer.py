
def check_emotional_warning(text: str):
    warning_words = ["selbstmord", "suizid", "verletzen"]
    if any(word in text.lower() for word in warning_words):
        warning = (
            "\u26a0\ufe0f Bitte suche professionelle Hilfe, wenn du Selbstgef\u00e4hrdung empfindest."
        )
        print(f"[Safety] {warning}")
        return warning
    return None
