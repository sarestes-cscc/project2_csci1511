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
            print("\nYou have requested a need audit. Please see below for our findings.")
            print("\nMocci cat also had input that he forced us to add. We do not take credit for his notes.")

            # Print this to JSON file
            need_levels = {
                 "Hunger Level": self.needs.hunger,
                 "Happiness Level": self.needs.happiness,
                 "Energy Level": self.needs.energy,
            }

            for key, value in need_levels.items():
                 print(f"\n{key}: {value}")

            self.print_mocci_notes()


    def print_mocci_notes(self):
         """"""
         pass