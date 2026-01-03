from functions_sal import roll_dice


def user_turn():
    """Handle one dice roll for the user and return the value."""
    while True:
        user_input = input("Press ENTER to roll the dice: ")
        if user_input == "":
            roll = roll_dice()
            print("-" * 10)
            print("You rolled:", roll)
            print("-" * 10)
            return roll
        else:
            print("Just press ENTER (no text) to roll.")




if __name__ == '__main__':
    user_turn()