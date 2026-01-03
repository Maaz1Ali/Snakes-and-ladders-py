import random


SNAKES = {
    99: 2,
    97: 81,
    95: 75,
    92: 88,
    79: 54,
    71: 55,
    25: 3,
}

LADDERS = {
    2: 37,
    11: 74,
    17: 44,
    33: 89,
    40: 85,
    51: 98,
    63: 95,
    70: 93,
}


def apply_snakes_ladders(position: int) -> int:
    """Return new position after checking for snake or ladder."""
    if position in SNAKES:
        print("🐍 Oops, snake bite! Down from", position, "to", SNAKES[position])
        return SNAKES[position]

    if position in LADDERS:
        print("🪜 Yay, ladder! Up from", position, "to", LADDERS[position])
        return LADDERS[position]

    return position


def roll_dice() -> int:
    """Return a random dice value between 1 and 6."""
    return random.randint(1, 6)



