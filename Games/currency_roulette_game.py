"""
currency_roulette_game.py Contains functions to implement the game number 3
"""

from random import randrange
from currency_converter import CurrencyConverter
from score import add_score


def get_money_interval():
    rand_number = randrange(1, 101)
    return [rand_number, usd_to_ils(rand_number)]


def get_guess_from_user(rand_number_usd):
    user_guess = input(f'The number in dollars is: {rand_number_usd}$ , now try to guess in shekels: ')
    return user_guess


def compare_results(rand_number_ils, user_guess, game_difficulty):
    deviation = 10 - game_difficulty
    if abs(float(rand_number_ils) - float(user_guess)) <= deviation:
        return True
    return False


def usd_to_ils(amount):
    c = CurrencyConverter()
    return c.convert(amount, 'USD', 'ILS')


def play(game_difficulty):
    [rand_number_usd, rand_number_ils] = get_money_interval()
    user_guess = get_guess_from_user(rand_number_usd)
    if compare_results(rand_number_ils, user_guess, game_difficulty):
        score = add_score(game_difficulty)
        print(f"You are a genius! You made it!\nThis time you got {score} points!")
    else:
        print("This time it didn't work, try again!")
