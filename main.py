

def main():
    """Main game function"""
    while True:
        print("Welcome to My Virtual Pet")
        print("...")
        print("Your pet's name is Mocci and humans know them to be of the species known as 'Cat'")
        print("...")
        print("Please pick an option from below to care for your cat known as Mocci.")

        main_menu()
        
        action = get_input()
        if action == "q":
            break


def main_menu():
    """Main menu selection process"""
    menu = {
        1: "Give your pet sustenance (Feed)", 
        2: "Play with magic light (Laser)",
        3: "Put pet in nest for regeneration (Sleep)",
        4: "Audit pet's need levels (Mood Checker)",    
    }

    for key, value in menu.items():
        print(f"{key}: {value}")

    menu_selection = input("Your choice (1-4): ")



def get_input():
    """"""
    user_input = input("Please enter input: ")
    return user_input

main()