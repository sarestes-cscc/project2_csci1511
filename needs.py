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
        self.happiness = self.pet.happiness


    def print_treat_menu(self):
        """Prints treat menu"""
        treats = {
            1: "Fish shaped crackers (+10 hunger)",
            2: "Wet, chunky sustenance from can (+20 hunger)",
            3: "Flaky, green crazy dust (-5 hunger)",
        }

        print("...")
        print("...")
        print(f"Current hunger: {self.hunger}")
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

        print(f"\nCurrent Hunger level: {self.hunger}")
        print("...")
        print("...")
        return self.hunger



    def print_toy_menu(self):
        """Prints toy menu"""
        toys = {
            1: "Play with the magic light stick (laser)",
            2: "Play with the flimsy magic stick (cat wand)",
            3: "Play with the ball of fluffy string (yarn)",
        }

        print("...")
        print("...")
        print("\nWe are are still trying to understand what Mocci cat likes. Point value for each happiness item is unknown. ")
        print("\nWe begrudingly own the following Mocci cat happiness items:\n")

        for key, value in toys.items():
                    print(f"{key}: {value}")

        self.choose_toy()


    def choose_toy(self):
        """Allows player to choose from the toy menu"""
        toy_choice = input("\nPlease choose 1-3: ")
        toy_choice = int(toy_choice)
        
        self.calculate_happiness(toy_choice)


    def calculate_happiness(self, toy_choice):
        """Calculates new happiness based off toy choice"""     
        if toy_choice == 1:
            print("\nMocci the cat walks away from the most expensive happiness item, bored and uninterested.")
            print("\nMocci the cat seems to be of too high intelligence to fall for the magic light stick.")
            print("\n+ 0 happiness")

        if toy_choice == 2:
            play_time = input("\nPlease enter amount of time spent with Mocci and happiness item (ex: '15' for 15 minutes): ")
            play_time = int(play_time)

            if play_time >= 20:
                print("\nMocci the cat seems to enjoy the flimsy magic stick.")
                print("\n+ 15 happpiness")
                
                self.happiness += 15

            if play_time < 20:
                print("\nMocci the cat seems to be the opposite of the happy emotion. Maybe Mocci the cat wants to spend more time with its 'human'.")
                print("\n+ 5 happiness")
                
                self.happiness += 5

        if toy_choice == 3:
            print("\nMocci the cat seems thrilled about any time spent with its 'human' and the ball of fluffy string.")
            print("\n+ 20 happiness")

            self.happiness += 20

        print(f"\nCurrent happiness level: {self.happiness}")
        print("...")
        print("...")
        return self.happiness