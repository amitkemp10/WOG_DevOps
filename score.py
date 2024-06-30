
from utils import SCORES_FILE_NAME


def add_score(difficulty):
    get_until_now_score = 0
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            get_until_now_score = file.read().strip()
    except FileNotFoundError:
        print(f"{SCORES_FILE_NAME} does not exist. Creating a new file.")
    calc_current_score = difficulty * 3 + 5
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(calc_current_score + int(get_until_now_score)))
    file.close()
    return calc_current_score
