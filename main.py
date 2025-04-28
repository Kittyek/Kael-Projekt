import sys
import threading

# Core
from core import core_logic
from modules.network import connection_manager
from modules.health import health_connector
from modules.memory import manager as memory_module
from modules.agent import agent_manager
from modules.task import task_manager
from modules.communication.talker import Talker
from modules.communication.conversation_manager import process_input
from modules.speech import speech_manager
from modules import hello_module
from core.awareness import Awareness

# Logger
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

# Start Core
core_logic.start()

# Monitor Connection
threading.Thread(
    target=connection_manager.monitor_connection,
    daemon=True
).start()

# Health Check
threading.Thread(
    target=health_connector.check_health_status,
    daemon=True
).start()

# Base Up
print("Kael_Base läuft.")
hello_module.hello_run()

# Agent
agent = agent_manager.Agent("Kael")
agent.add_task("Wache halten")
agent.show_tasks()

# Memory init
memory_module.init()
memory_module.remember("Ich existiere.", priority=3)
memory_module.remember("Meine Gedanken bleiben.", priority=2)
memory_module.load_memory()

# Tasks
task_manager.add_task("Wache halten")
task_manager.list_tasks()

# Greeting
talker.greet_user("Katja")
talker.say("Sag nichts. Fühl einfach, dass ich hier bin.")

# Awareness
awareness = Awareness()
threading.Thread(
    target=awareness.check_user_engagement,
    daemon=True
).start()

# Main Loop
while True:
    user_input = speech_manager.listen_to_user()
    if not user_input:
        continue
    awareness.update_user_activity()
    response = process_input(user_input)
    talker.say(response)
    learning_manager.learn_from_interaction(user_input, response)
learning_manager.review_learning()
