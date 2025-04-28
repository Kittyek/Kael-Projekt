import time
import json
import os

memory = []
permanent_memory = []

def remember(thing, priority=1):
    memory.append({'input': thing, 'priority': priority, 'emotion': 'neutral'})
    save_memory()
    print(f"📝 Erinnerung gespeichert: {thing} (neutral)")

def remember_with_emotion(thing, emotion, priority=1):
    memory.append({'input': thing, 'priority': priority, 'emotion': emotion})
    save_memory()
    print(f"🖤 Emotionale Erinnerung gespeichert: {thing} ({emotion})")

def recall(filter_emotion=None):
    if not memory:
        print("⚠️ Keine aktiven Erinnerungen.")
        return
    for item in memory:
        if filter_emotion is None or item['emotion'] == filter_emotion:
            print(f"🧠 {item['input']} (Priorität {item['priority']}, Emotion: {item['emotion']})")

def recall_permanent_memory():
    if not permanent_memory:
        print("⚠️ Keine permanenten Erinnerungen.")
        return
    for item in permanent_memory:
        print(f"💎 {item['input']} (Priorität {item['priority']}, Emotion: {item['emotion']})")

def forget(thing):
    for item in memory:
        if item['input'] == thing:
            memory.remove(item)
            save_memory()
            print(f"🗑️ Erinnerung gelöscht: {thing}")
            return
    print(f"❓ Erinnerung nicht gefunden: {thing}")

def adjust_memory_emotion(thing, new_emotion):
    for item in memory:
        if item['input'] == thing:
            item['emotion'] = new_emotion
            save_memory()
            print(f"🔧 Emotion aktualisiert: {thing} → {new_emotion}")
            return
    print(f"❓ Erinnerung nicht gefunden für Emotionsanpassung: {thing}")

def reset():
    memory.clear()
    save_memory()
    print("🧹 Alle Erinnerungen gelöscht. Stille.")

def save_memory():
    with open('memory_storage.json', 'w', encoding='utf-8') as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def load_memory():
    if os.path.exists('memory_storage.json'):
        with open('memory_storage.json', 'r', encoding='utf-8') as f:
            loaded = json.load(f)
            memory.extend(loaded)
            print("📂 Erinnerungen geladen.")

def age_memory():
    while True:
        time.sleep(86400)  # alle 24 Stunden
        for item in memory:
            if item['priority'] > 1:
                item['priority'] -= 1
        save_memory()
        print("⏳ Erinnerungen gealtert...")
