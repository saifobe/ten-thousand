from ten_thousand.game_logic import GameLogic
roll_dice = GameLogic.roll_dice
points_calculate = GameLogic.calculate_score


def play(roller=GameLogic.roll_dice):
    global roll_dice
    roll_dice = roller

    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user_res = input('> ')
    if user_res == "n":
        quitter()
    if user_res == 'y':
        start_game()


def quitter():
    """quit the game"""
    return print('OK. Maybe another time')


def start_game(round_num=1, total=0, number_dices=6):
    """start the game and call the functions to play the game and calculate the points and the total points and the round number and the number of dices to roll in the next round"""
    
    user_choice = ''
    first_roll = roll_dice(number_dices)
    # zilch test
    if points_calculate(first_roll) == 0:
        print("ohhh ohhh ZILTCH you Lost your points.")
        round_num += 1
        points = 0
        return start_game(round_num, total, number_dices=6)
    
    unpacked_tuple = ''

    for i in first_roll:
        unpacked_tuple += str(i)+' '
    print(f'Starting round {round_num}')
    print(f'Rolling {number_dices} dice...')
    print("*** "+unpacked_tuple.strip()+' ***')
    print("Enter dice to keep, or (q)uit:")
    user_choice = input('> ')

    if user_choice == "q":
        end_game(total)

    else:
        dice_to_keep = tuple(int(x) for x in user_choice)
        roll_to_test_cheater = list(first_roll)

        for i in dice_to_keep:
            if i not in roll_to_test_cheater:
                print("""********************************************\n********************************************\n***************  DON'T CHEAT  **************\n********************************************\n********************************************\n                TRY AGAIN   """)
                return start_game(round_num, total, number_dices=6)
            index = roll_to_test_cheater.index(i)
            roll_to_test_cheater.pop(index)
        number_dices = number_dices - len(dice_to_keep)
        points = points_calculate(dice_to_keep)
        print(
            f"You have {points} unbanked points and {number_dices} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_choice = input('> ')
        if user_choice == 'q':
            end_game(total)
        elif user_choice == 'r':
            if number_dices > 0:
                points += points
                start_game(round_num, total, number_dices)
            else:
                print(
                    'you ran out of dices new round will start\n you didnt bank yor points so you lost them')
                round_num += 1
                start_game(round_num, total, number_dices=6)
        elif user_choice == "b":
            bank_points(points, round_num, total)


def bank_points(points, round_num, total):
    """bank points and start new round and add points to total points"""
    total = total + points
    print(f"You banked {points} points in round {round_num}")
    print(f"Total score is {total} points")
    round_num += 1
    start_game(round_num, total)


def end_game(total):
    """end game and print total points earned by the player and thank him for playing"""
    print(f"Thanks for playing. You earned {total} points")


if __name__ == "__main__":
    play()
