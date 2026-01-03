from functions_sal import roll_dice


def com_turn():
    """Handle one dice roll for the computer and return the value."""
    roll = roll_dice()
    print("-" * 10)
    print("Computer rolled:", roll)
    print("-" * 10)
    return roll


if __name__ == "__main__":
    com_turn()