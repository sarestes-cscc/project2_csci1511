

def main():
    """Main game function"""
    while True:
        print("Welcome to My Virtual Pet")
        print("...")
        print("Your pet's name is Mocci and humans know them to be of the species known as 'Cat'")
        print("...")
        print("Please pick an option from below to care for your cat known as Mocci.")

        action = get_input()
        if action == "q":
            break


def main_menu():
    pass



def get_input():
    """"""
    user_input = input("Please enter input: ")
    return user_input

main()