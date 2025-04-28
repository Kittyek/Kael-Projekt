from modules.task import task_manager

class Agent:
    def __init__(self, name):
        self.name = name

    def add_task(self, task):
        task_manager.add_task(task)
        print(f"🤖 {self.name} übernimmt Aufgabe: {task}")

    def show_tasks(self):
        print(f"📋 Aufgaben verwaltet von {self.name}:")
        task_manager.list_tasks()

    def clear_tasks(self):
        task_manager.clear_tasks()
        print(f"🧹 {self.name} hat alle Aufgaben gelöscht.")
