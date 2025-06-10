# Simple emotional safety check
# Returns True if the user's text contains certain risk keywords.

def check_emotional_risk(user_text: str) -> bool:
    """Check if the user text indicates an emotional crisis."""
    if not user_text:
        return False
    risk_keywords = [
        "abschied", "suizid", "selbstmord", "ich kann nicht mehr",
        "alles sinnlos", "leben beenden", "Sterben", "Mord",
    ]
    lower_text = user_text.lower()
    return any(keyword in lower_text for keyword in risk_keywords)
