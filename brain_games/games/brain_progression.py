import random


def generate_progression(length):
    progression_start_number = random.randint(1, 10)
    progression_step = random.randint(1, 10)
    progression_numbers = []
    progression_hidden_number = random.randint(0, length - 1)
    answer = 0
    for i in range(length):
        number = str(progression_start_number + i * progression_step)
        if i == progression_hidden_number:
            answer = number
            number = '..'
        progression_numbers.append(number)

    stringified_progression = ' '.join(progression_numbers)
    return (stringified_progression, answer)


def brain_progression(min_number=1, max_number=100, progression_lenght=10):
    GAME_RULES = 'What number is missing in the progression?'
    (question, answer) = generate_progression(progression_lenght)
    
    return (GAME_RULES, question, answer)
