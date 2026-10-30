""" 
    Main game file 
    Virtual pet terminal
"""


from needs import Needs
from pet import Pet


needs = Needs()


def main():
    """Main game function"""
    while True:
        print("Welcome to My Virtual Pet for 'Humans'")
        print("...")
        print("Your pet's name is Mocci and humans know them to be of the species known as 'Cat'")
        print("...")
        print("Please pick an option from below to care for your cat known as Mocci.\n")

        main_menu()

        action = get_input()
        if action == "q":
            break


def main_menu():
    """Main menu selection process"""
    menu = {
        1: "Give your pet sustenance (Feed)", 
        2: "Play with unnecessary items bought for happiness (Play)",
        3: "Put pet in nest for regeneration (Sleep)",
        4: "Audit pet's need levels (Mood Checker)",    
    }

    for key, value in menu.items():
        print(f"{key}: {value}")

    menu_selection = input("\nYour choice (1-4): ")
    menu_selection = int(menu_selection)

    menu_route(menu_selection)


def menu_route(menu_selection):
    """Routes player based on menu selection"""
    if menu_selection == 1:
        needs.print_treat_menu()

    if menu_selection == 2:
        needs.print_toy_menu()

    if menu_selection == 3:
        # sleep() # method in Needs class
        pass

    if menu_selection == 4:
        # mood() # method in Pet class
        pass


def get_input():
    """ just here for testing """
    user_input = input("Please enter input: ")
    return user_input

main()