"""
    Need audit methods - JSON file will be used here to track need audits if multiple are called before 
    game ends. Print the audits to the terminal as well
"""

import json

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
        print("You can see past audits in the audit.json file. Delete this file to reset it.\n")

        # Print this to JSON file
        need_levels = {
            "Hunger Level": self.needs.hunger,
            "Happiness Level": self.needs.happiness,
            "Energy Level": self.needs.energy,
        }

        for key, value in need_levels.items():
            print(f"{key}: {value}")

        if self.needs.hunger < 80 or self.needs.happiness < 60 or self.needs.energy <= 30:
            self.mocci_ouput()

        print("\n...")
        print("...\n")

        self.json_dump(need_levels)


    def mocci_ouput(self):
        print("\nMocci cat forced additional notes upon us. This is what Mocci cat had to say about his current state:")

        if self.needs.happiness < 60:
            mocci_note_happiness = ("\n'My happiness is decreasing human. I demand you play with me and my fluffy string ball.'")
            print(mocci_note_happiness)

        if self.needs.hunger < 80:
            mocci_note_hunger = ("\n'I am demanding food now. You must run and fetch food, human! I will not wait.'")
            print(mocci_note_hunger)

        if self.needs.energy <= 30:
            mocci_note_energy = ("\n'Do not bother me, human. I am too tired to deal with you.'")
            print(mocci_note_energy)


    def json_dump(self, need_levels):
        with open("audit.json", "a") as file:
            file.write(json.dumps(need_levels) + "\n")
