import prompt


def game_engine(name, game, attempts=3):
    (game_rules, *_) = game()
    print(game_rules)
    
    for _ in range(attempts):
        (_, question, answer) = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct!')
            continue
        else: 
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was\
                    '{answer}'.\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

