import random


def brain_calc(min_num=1, max_num=100):
    MATH_SIGNS = ['+', '-', '*']
    GAME_RULES = 'What is the result of the expression?'
    operator = MATH_SIGNS[random.randint(1, 2)]
    first_num = random.randint(min_num, max_num)
    second_num = random.randint(min_num, max_num)
    question = f'{max(first_num, second_num)} {operator}\
            {min(first_num, second_num)}'
    match operator:
        case '+':
            answer = first_num + second_num
        case '-':
            answer = abs(first_num - second_num)
        case '*':
            answer = first_num * second_num

    answer = str(answer)

    return (GAME_RULES, question, answer)
