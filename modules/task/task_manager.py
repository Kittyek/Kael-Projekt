tasks = []

def add_task(task):
    tasks.append(task)
    print(f"📝 Neue Aufgabe hinzugefügt: {task}")

def list_tasks():
    if tasks:
        print("\n🗒️ Aufgabenliste:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\n🗒️ Keine Aufgaben vorhanden.")

def clear_tasks():
    tasks.clear()
    print("🧹 Alle Aufgaben wurden gelöscht.")
