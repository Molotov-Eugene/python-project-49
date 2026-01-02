from brain_games.scripts.welcome_user import welcome_user


def main():
    name = welcome_user()
    print(f'Hello, {name}!')


if __name__ == "__main__":
    main()
