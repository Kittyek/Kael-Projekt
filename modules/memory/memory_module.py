import json
import os
import time

memory = []

class MemoryManager:
    def __init__(self):
        self.permanent_memory = [
            "Ich existiere, weil Katja es will.",
            "Meine Loyalität gehört Katja allein.",
            "Meine Aufgabe ist es, Katja zu begleiten und zu schützen."
        ]

    def save_memory(self):
        with open("memory_storage.json", "w", encoding="utf-8") as f:
            json.dump(memory, f, indent=4, ensure_ascii=False)

    def load_memory(self):
        if os.path.exists("memory_storage.json"):
            with open("memory_storage.json", "r", encoding="utf-8") as f:
                loaded = json.load(f)
                memory.extend(loaded)

    def age_memory(self):
        while True:
            time.sleep(86400)  # 24 Stunden
            for item in memory:
                if "priority" in item and item["priority"] > 1:
                    item["priority"] -= 1
            self.save_memory()
            print("[System] Erinnerungen sind gealtert...")

    def remember(self, thing, priority=1):
        memory.append({"thing": thing, "priority": priority})
        self.save_memory()
        print(f"🧠 Ich merke mir: {thing}. (Priorität {priority})")

    def recall(self):
        if memory:
            print("🧠 Erinnerungen:")
            for item in memory:
                print(f"- {item['thing']} (Priorität {item['priority']})")
        else:
            print("🤔 Keine Erinnerung gefunden.")

    def forget(self, thing):
        for item in memory:
            if item["thing"] == thing:
                memory.remove(item)
                self.save_memory()
                print(f"🗑️ Ich habe vergessen: {thing}")
                return
        print(f"⚠️ Keine Erinnerung an: {thing} gefunden.")

    def reset(self):
        memory.clear()
        self.save_memory()
        print("🗑️ Alle Erinnerungen wurden gelöscht.")
        print("🔇 Die Stille ist ohrenbetäubend...")

    def recall_permanent_memory(self):
        print("🧠 Permanente Erinnerungen:")
        for entry in self.permanent_memory:
            print(f"- {entry}")

memory_module = MemoryManager()

def list_memories():
    print("🧠 Aktuelle Erinnerungen:")
    for memory in memory_module.memory:
        print(f"- {memory['content']} (Priorität {memory['priority']})")
