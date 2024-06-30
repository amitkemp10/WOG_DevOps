"""
app.py contains functions for welcoming users and starting game play.
"""

from Games import guess_game, currency_roulette_game, memory_game
from utils import screen_cleaner


def welcome():
    while True:
        name = input("\nPlease enter your name: ")
        if check_name(name):
            break
    print("""
    *******************************************************************
    \tHi {} and welcome to the World of Games: The Epic Journey
    """.format(name))


def start_play():
    while True:
        game_number = input("Please choose a game to play: \n\t1. Memory Game - a sequence of numbers will appear for 1"
                            "second and you"
                            "have"
                            "to guess it back.\n\t2. Guess Game - guess a number and see if you chose like the "
                            "computer."
                            "\n\t3. Currency"
                            "Roulette - try and guess the value of a random amount of USD in ILS\n\t   Enter your "
                            "choice: ")
        if check_game_number(game_number):
            break
    game_number = int(game_number)
    while True:
        game_difficulty = input("\nPlease select a difficulty level between 1 and 5: ")
        if check_game_difficulty(game_difficulty):
            break
    game_difficulty = int(game_difficulty)
    print("*******************************************************************\n")
    screen_cleaner()
    if game_number == 1:
        memory_game.play(game_difficulty)
    elif game_number == 2:
        guess_game.play(game_difficulty)
    else:
        currency_roulette_game.play(game_difficulty)


def check_name(name):
    if not name.isalpha():
        print("Name must contain only letters, please try again")
        return False
    return True


def check_game_number(game_number):
    games_options = [1, 2, 3]
    if not game_number.isdigit() or int(game_number) not in games_options:
        print("\nEnter an appropriate game number, please try again\n")
        return False
    return True


def check_game_difficulty(game_difficulty):
    difficulty_options = range(1, 6)
    if not game_difficulty.isdigit() or int(game_difficulty) not in difficulty_options:
        print("Enter an appropriate difficulty level, please try again")
        return False
    return True
