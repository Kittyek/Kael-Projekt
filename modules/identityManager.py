_identity = "Kael"

def set_identity(name: str):
    global _identity
    _identity = name
    print(f"[Identity] Identität gesetzt auf {name}")


def get_identity() -> str:
    return _identity
