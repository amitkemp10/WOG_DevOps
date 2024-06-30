"""
memory_game.py Contains functions to implement the game number 1
"""

import time
from random import randrange
from utils import screen_cleaner
from score import add_score


def generate_sequence(game_difficulty):
    random_list = list(range(game_difficulty))
    for i in range(len(random_list)):
        random_list[i] = randrange(1, 101)
    return random_list


def get_list_from_user(random_list):
    print('The list of numbers to remember:')
    print(random_list)
    time.sleep(0.7)
    screen_cleaner()
    user_input = input(f'Now, insert the numbers in the same length and in the same order: ').split(',')
    user_list = [int(num) for num in user_input]
    return user_list


def is_list_equal(random_list, user_list):
    if random_list == user_list:
        return True
    return False


def play(game_difficulty):
    random_list = generate_sequence(game_difficulty)
    user_list = get_list_from_user(random_list)
    if is_list_equal(random_list, user_list):
        score = add_score(game_difficulty)
        print(f"You are a genius! You made it!\nThis time you got {score} points!")
    else:
        print("This time it didn't work, try again!")
