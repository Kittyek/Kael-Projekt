# simple adaptive response trainer

_response_bank = {
    "glücklich": "Ich freue mich für dich!",
    "traurig": "Ich bin bei dir, wenn du mich brauchst.",
    "wütend": "Lass uns einen Moment durchatmen.",
}

def get_best_response(mood: str):
    """Gibt eine vordefinierte Antwort zur Stimmung zurück."""
    return _response_bank.get(mood)
