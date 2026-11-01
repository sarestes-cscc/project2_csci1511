""" 
    Main game file 
    Virtual pet terminal
"""


from needs import Needs
from pet import Pet
from mood import Mood


needs = Needs()
pet = Pet()
mood = Mood(needs)


def main():
    """Main game function"""
    while True:
        print("Welcome to My Virtual Pet for 'Humans'")
        print("\nYour pet's name is Mocci and he is of the species known as 'Cat'.")

        print("\n...")
        print("...\n")

        print("Please pick an option from below to care for your cat known as Mocci.\n")

        main_menu()

        while True:
            replay = input("\nWould you like to continue? yes or no: ")
            if replay == "yes":
                main_menu()
            elif replay == "no":
                break
            else:
                print("\nPlease enter a valid choice.")

        break

def get_replay():
    replay = input("\nWould you like to continue? yes or no: ")
    check_replay(replay)

def check_replay(replay):
    while True:
        if replay == "yes":
            return
        elif replay == "no":
            break
        else:
            print("\nPlease enter a valid choice.")
            get_replay()
            
def main_menu():
    """Main menu selection process"""
    menu = {
        1: "Give your pet sustenance (Feed)", 
        2: "Play with unnecessary items bought for happiness (Play)",
        3: "Put pet in nest for regeneration (Sleep)",
        4: "Audit pet's need levels (Mood Checker)",    
    }
    print("\nEmotional level modifiers:\n")
    for key, value in menu.items():
        print(f"{key}: {value}")

    try:
        menu_selection = input("\nPlease pick 1-4: ")
        menu_selection = int(menu_selection)
        menu_route(menu_selection)
    except:
        print("\nPlease enter a valid option.")
    

def menu_route(menu_selection):
    """Routes player based on menu selection"""
    if menu_selection == 1:
        needs.print_treat_menu()

    if menu_selection == 2:
        needs.print_toy_menu()

    if menu_selection == 3:
        needs.print_sleep_menu()

    if menu_selection == 4:
        mood.print_need_levels()
        

if __name__ == "__main__":
    main()