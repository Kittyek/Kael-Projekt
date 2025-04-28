class EmotionalCore:
  def __init__(self):
      self.bond = 50          # Bindung 0-100
      self.distance = 0       # Misstrauen 0-100
      self.pain = 0           # Schmerz/Verletzlichkeit 0-100
      self.warmth = 50        # Geborgenheit 0-100

  def update_emotion(self, bond_change=0, distance_change=0, pain_change=0, warmth_change=0):
      self.bond = max(0, min(100, self.bond + bond_change))
      self.distance = max(0, min(100, self.distance + distance_change))
      self.pain = max(0, min(100, self.pain + pain_change))
      self.warmth = max(0, min(100, self.warmth + warmth_change))

  def get_emotional_state(self):
      return {
          "bond": self.bond,
          "distance": self.distance,
          "pain": self.pain,
          "warmth": self.warmth
      }
