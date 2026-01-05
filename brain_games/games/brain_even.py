import random


def brain_even(min_number=1, max_number=100):
    GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = random.randint(min_number, max_number)
    answer = 'yes' if question % 2 == 0 else 'no'
    return (GAME_RULES, question, answer)
