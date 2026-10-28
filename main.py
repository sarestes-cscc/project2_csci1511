

def main():
    """Main game function"""
    while True:
        action = get_input()
        if action == "q":
            break

def get_input():
    """"""
    user_input = input("Please enter input: ")
    return user_input

main()