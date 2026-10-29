"""
    Needs Class methods
    Hunger, Energy, Play
"""

from pet import Pet


class Needs:
    """"""
    def __init__(self):
        self.pet = Pet()
        self.hunger = self.pet.hunger


    def print_menu(self):
        """Prints treat menu"""
        treats = {
            1: "Fish shaped crackers (+10 hunger)",
            2: "Wet, chunky sustenance from can (+20 hunger)",
            3: "Flaky, green crazy dust (-5 hunger)",
        }

        print("\nThe sustenance options are:\n")

        for key, value in treats.items():
            print(f"{key}: {value}")

        self.choose_treat()


    def choose_treat(self):
        """Allows player to choose from treat menu"""
        treat_choice = input("\nPlease choose 1-3: ")
        treat_choice = int(treat_choice)

        print("\nMmmm the Mocci cat seemed to enjoy that treat.")

        self.calculate_hunger(treat_choice)


    def calculate_hunger(self, treat_choice):
        """Caculates new Hunger based off of treat choice from choose_treat()"""
        if treat_choice == 1:
            self.hunger += 10

        if treat_choice == 2:
            self.hunger += 20

        if treat_choice == 3:
            self.hunger -= 5

        print(f"\n{self.hunger}")
        return self.hunger
