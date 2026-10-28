

def main():
    """Main game function"""
    setup()
    while True:
        show_state()
        action = get_input()

        if action == "q":
            break
        update(action)

        if game_over():
            break

    show_ending()


def setup():
    """"""
    pass


def show_state():
    """"""
    pass


def get_input():
    """"""
    user_input = input("Please enter input: ")
    return user_input


def update(action):
    """"""
    pass


def game_over():
    """"""
    pass


def show_ending():
    """"""
    pass


main()