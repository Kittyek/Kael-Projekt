import json
import os

_CONTEXT_FILE = "context_history.json"

def get_context():
    if os.path.exists(_CONTEXT_FILE):
        with open(_CONTEXT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def update_context(mood, response, music=None, warning=None):
    context = get_context()
    context.append({
        "mood": mood,
        "response": response,
        "music": music,
        "warning": warning
    })
    with open(_CONTEXT_FILE, "w", encoding="utf-8") as f:
        json.dump(context, f, indent=2, ensure_ascii=False)
