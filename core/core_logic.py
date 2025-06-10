# core/core_logic.py

import threading
from modules.communication import talker
from modules.speech import speech_manager
from modules.memory import memory_module
from modules.agent.agent_manager import Agent
from modules.task import task_manager
from modules.learning.learning_manager import learning_manager
from modules.network.connection_manager import connection_manager
from modules.health.health_connector import health_connector
from modules.communication.conversation_manager import process_input
from core.awareness import Awareness
from emotionalSafetyLayer import check_emotional_risk

def start():
    """Starte alle Subsysteme und den Haupt-Dialog-Loop."""
    # --- Subsystem-Threads ---
    threading.Thread(target=connection_manager.monitor_connection, daemon=True).start()
    threading.Thread(target=health_connector.check_health_status, daemon=True).start()

    awareness = Awareness()
    threading.Thread(target=awareness.check_user_engagement, daemon=True).start()

    # --- Initialisierung ---
    print("Kael_Base läuft.")
    # (hier können wir noch Tasks/Agent initialisieren etc.)

    # Endlos-Loop
    while True:
        # 1) Eingabe holen (Sprache oder Text)
        user_input = speech_manager.listen_to_user()

        # Nach der Eingabe auf emotionale Krisensignale prüfen
        if check_emotional_risk(user_input):
            print("⚠️ Kippmoment erkannt – ich bin da.")

        # 2) Awareness updaten
        awareness.update_user_activity()

        # 3) Input verarbeiten & Antwort erzeugen
        response = process_input(user_input)

        # 4) Antwort ausgeben
        talker.say(response)

        # 5) Aus der Interaktion lernen
        learning_manager.learn_from_interaction(user_input, response)
