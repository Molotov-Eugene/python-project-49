import random


def brain_gcd(min_number=1, max_number=100):
    GAME_RULES = 'Find the greatest common divisor of given numbers.'
    first_number = random.randint(min_number, max_number)
    second_number = random.randint(min_number, max_number)
    question = f'{first_number} {second_number}'
    
    answer = first_number
    temp_number = second_number
    while temp_number != 0:
        (temp_number, answer) = (answer % temp_number, temp_number)
    answer = str(answer)
    return (GAME_RULES, question, answer)
