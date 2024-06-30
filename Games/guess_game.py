"""
guess_game.py Contains functions to implement the game number 2
"""


from random import randrange
from score import add_score


def generate_number(game_difficulty):
    print('The computer picked a number in the range')
    return randrange(game_difficulty + 1)


def get_guess_from_user(game_difficulty):
    chosen_number = input(f'Please choose a number between 0 to {game_difficulty}: ')
    return chosen_number


def compare_results(secret_number, user_input):
    if secret_number == user_input:
        return True
    return False


def play(game_difficulty):
    secret_number = generate_number(game_difficulty)
    user_input = int(get_guess_from_user(game_difficulty))
    if compare_results(secret_number, user_input):
        score = add_score(game_difficulty)
        print(f"You are a genius! You made it!\nThis time you got {score} points!")
    else:
        print("\nThis time it didn't work, try again!")
