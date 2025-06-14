class LearningSystem:
    def __init__(self):
        self.memory = []
        self.history = []

    def learn_from_interaction(self, input_data, response_data):
        self.memory.append({
            "input": input_data,
            "response": response_data
        })
        self.history.append(f"Learned: {input_data} -> {response_data}")
        print(f"💬 Kael hat gelernt: {input_data} -> {response_data}")

    def review_learning(self):
        print("📖 Review des Gelernten:")
        for entry in self.history:
            print(entry)

# global Instanz, damit andere Module darauf zugreifen können
learning_manager = LearningSystem()

def start_learning_cycle():
    print("[Learning] (Simulation) Lernzyklus gestartet... (auf Replit deaktiviert)")
