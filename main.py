""" 
    Main game file 
    Virtual pet terminal
"""


from needs import Needs
from pet import Pet


needs = Needs()
pet = Pet()


def main():
    """Main game function"""
    while True:
        print("Welcome to My Virtual Pet for 'Humans'")
        print("\nYour pet's name is Mocci and he is of the species known as 'Cat'.")

        print("\n...")
        print("...\n")

        print("Please pick an option from below to care for your cat known as Mocci.\n")

        main_menu()

        replay = input("Would you like to continue? y or n: ")
        print("\n...")
        print("...\n")

        if replay == "n":
            break


def main_menu():
    """Main menu selection process"""
    menu = {
        1: "Give your pet sustenance (Feed)", 
        2: "Play with unnecessary items bought for happiness (Play)",
        3: "Put pet in nest for regeneration (Sleep)",
        4: "Audit pet's need levels (Mood Checker)",    
    }
    print("Emotional level modifiers:\n")
    for key, value in menu.items():
        print(f"{key}: {value}")

    menu_selection = input("\nPlease pick 1-4: ")
    menu_selection = int(menu_selection)

    menu_route(menu_selection)


def menu_route(menu_selection):
    """Routes player based on menu selection"""
    if menu_selection == 1:
        needs.print_treat_menu()

    if menu_selection == 2:
        needs.print_toy_menu()

    if menu_selection == 3:
        needs.print_sleep_menu()

    if menu_selection == 4:
        # mood() # method in Pet class
        pass


main()