from user_game import user_turn
from com_game import com_turn
from functions_sal import apply_snakes_ladders


def main():
    user_position = 0
    com_position = 0

    print("-" * 40)
    print("WELCOME TO SNAKES AND LADDERS")
    print("First to reach exactly 100 wins!")
    print("-" * 40)

    while True:
        try:
            # ---------- USER TURN ----------
            print("Your turn:")
            roll = user_turn()
            user_position += roll

            if user_position > 100:
                # cannot move beyond 100
                user_position -= roll
                print("| |"*10)
                print("You need exactly", 100 - user_position, "to win.")
                print("| |"*10)
            user_position = apply_snakes_ladders(user_position)
            print("Your position is:", user_position)
            print("-" * 40)
            if user_position == 100:
                print("" + "-" * 40)
                print("🎉 You won the game!")
                print("-" * 40)
                break

            # ---------- COMPUTER TURN ----------
            print("Computer's turn:")
            roll = com_turn()
            com_position += roll

            if com_position > 100:
                com_position -= roll
                print("| |"*10)
                print("Computer needs exactly", 100 - com_position, "to win.")
                print("| |"*10)

            com_position = apply_snakes_ladders(com_position)
            print("Computer position is:", com_position)
            print("-" * 40)

            if com_position == 100:
                print("" + "-" * 40)
                print("💻 Computer won the game!")
                print("You Lost the game!")
                print("-" * 40)
                break

        except (EOFError, KeyboardInterrupt):
            print("Game interrupted. Goodbye!")
            break


if __name__ == "__main__":
    main()