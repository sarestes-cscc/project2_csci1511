"""
    Virtual Pet Simulator
    Sarah Estes 11/1/27
    Holds default values for need levels
"""

class Pet:
    """Settings class to hold the defaults for hunger, happiness, and energy"""
    def __init__(self):
        """Initializing default levels"""
        self.hunger = 20
        self.happiness = 50
        self.energy = 80
