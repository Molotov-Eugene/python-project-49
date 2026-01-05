import random


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6

    return True


def brain_prime():
    GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'

    return (GAME_RULES, question, answer)
