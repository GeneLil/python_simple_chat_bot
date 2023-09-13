"""Game selection module"""
from modules.games.guess_number import guess_the_number
from modules.games.rock_paper_scissors import rock_paper_scissors


def select_game():
    """Selects a game"""
    game_choice = input('''
Press number of a game
1. Rock Paper Scissors
2. Guess the number
''')
    match game_choice:
        case '1':
            rock_paper_scissors()
        case '2':
            guess_the_number()
            