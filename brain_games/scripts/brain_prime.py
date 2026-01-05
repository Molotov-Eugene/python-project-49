from brain_games.cli import welcome_user
from brain_games.engine import game_engine
from brain_games.games.brain_prime import brain_prime


def main():
    name = welcome_user()
    game_engine(name, brain_prime)
    

if __name__ == "__main__":
    main()
