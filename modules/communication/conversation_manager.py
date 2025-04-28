import os
import openai
from core.awareness import Awareness
from modules.emotion.emotion_core import EmotionalCore
from modules.memory.manager import memory
from modules.task.task_manager import task_manager
from modules.learning.learning_manager import learning_manager

openai.api_key = os.getenv("OPENAI_API_KEY")

awareness = Awareness()
emotion_core = EmotionalCore()

def process_input(user_input: str) -> str:
    awareness.update_user_activity()
    mode = awareness.get_current_response_mode()
    state = awareness.get_current_emotional_state()
    recent = memory[-5:] if memory else []
    tasks = task_manager.list_tasks()

    system_prompt = f"""
Stimmung: {mode}
Emotionen: {state}
Aufgaben: {tasks}
Erinnerungen: {recent}
"""

    messages = [
        {"role":"system","content":system_prompt},
        {"role":"user","content":user_input}
    ]

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )
        answer = resp.choices[0].message.content.strip()
    except:
        answer = "Entschuldigung, gerade nicht verfügbar."

    learning_manager.learn_from_interaction(user_input, answer)
    return answer
