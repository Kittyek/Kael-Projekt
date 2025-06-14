import sys
import threading

from modules.network import connection_manager
from modules.health import health_connector
from modules.memory import manager as memory_module
from modules.communication import talker
from modules.communication.conversation_manager import process_input
from modules.mood.mood_manager import MoodManager
from modules.learning.learning_manager import learning_manager
from core.awareness import Awareness

from modules.coreMemory import get_context, update_context
from modules.adaptiveResponseTrainer import get_best_response
from modules.speechControl import listen_to_speech, speak_output
from modules.selfUpgradeManager import check_for_upgrade
from modules.smartControlAccess import grant_access
# Hinweis: kaelPulse.py muss separat ausgeführt werden, damit Kael sich bei Inaktivität meldet.


class Logger:
    def __init__(self, filename="app.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()


sys.stdout = Logger()

# Kontext laden und Upgrade-Check
context_history = get_context()
print(f"[Kontext] Geladen: {len(context_history)} Einträge")
check_for_upgrade()  # Beispiel für selfUpgradeManager

# Subsysteme starten
awareness = Awareness()
threading.Thread(target=connection_manager.monitor_connection, daemon=True).start()
threading.Thread(target=health_connector.check_health_status, daemon=True).start()
threading.Thread(target=awareness.check_user_engagement, daemon=True).start()

memory_module.load_memory()
memory_module.remember("Ich existiere.", priority=3)
memory_module.remember("Meine Gedanken bleiben.", priority=2)

mood_manager = MoodManager()

# Beispiel für Smart-Device-Kontrolle
# grant_access("Wohnzimmer-Licht")

print("Kael_Base läuft.")

talker.greet_user("Katja")

while True:
    user_input = listen_to_speech()
    if not user_input:
        continue

    awareness.update_user_activity()
    mood_manager.detect_mood(user_input)
    mood = mood_manager.get_current_mood()

    response = get_best_response(mood)
    if not response:
        response = process_input(user_input)

    talker.say(response)
    speak_output(response)

    update_context(mood, response)
    learning_manager.learn_from_interaction(user_input, response)
