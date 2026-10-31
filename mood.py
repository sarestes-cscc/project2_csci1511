"""
    Need audit methods - JSON file will be used here to track need audits if multiple are called before 
    game ends. Print the audits to the terminal as well
"""

from needs import Needs

class Mood:
    """Handles mood and need level actions"""
    def __init__(self, needs_instance):
        """Initializes updated levels from Needs class"""
        self.needs = needs_instance


    def print_need_levels(self):
        """Intro to need audit and prints need levels"""
        print("\n...")
        print("...\n")
        print("\nYou have requested a need audit. Please see below for our findings.\n")

        # Print this to JSON file
        need_levels = {
            "Hunger Level": self.needs.hunger,
            "Happiness Level": self.needs.happiness,
            "Energy Level": self.needs.energy,
        }

        for key, value in need_levels.items():
            print(f"{key}: {value}")

        if self.needs.hunger < 80 or self.needs.happiness < 60 or self.needs.energy <= 30:
            self.print_mocci_notes()


    def print_mocci_notes(self):
        """"""
        print("\nMocci cat forced additional notes upon us. This is what Mocci cat had to say about his current state:")

        if self.needs.happiness < 60:
            print("\n'My happiness is decreasing human. I demand you play with me and my fluffy string ball.'")

        if self.needs.hunger < 80:
            print("\n'I am demanding food now. You must run and fetch food, human! I will not wait.'")

        if self.needs.energy <= 30:
            print("\n'Do not bother me, human. I am too tired to deal with you.'")

        print("\n...")
        print("...\n")
