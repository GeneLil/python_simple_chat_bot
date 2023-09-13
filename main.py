"""Chat bot"""
import pyjokes
from script_background_music import play_music_in_background
from games.rock_paper_scissors import rock_paper_scissors
from games.guess_number import guess_the_number
from recommend_movie import print_movies


def tell_a_joke():
    """Tell a joke"""
    print(pyjokes.get_joke('en', category='all'))


def main_menu_choice():
    """Draws main menu"""
    return input('''
Menu:
1. Tell a joke to start the day!
2. Recommend a movie.
3. Play a game.
4. Exit
''')


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


def draw_menu():
    """Drawing main menu"""
    print('Hello! I\'m a chat bot and here\'s what I can do: ')
    while True:
        choice = main_menu_choice()
        match choice:
            case '1':
                tell_a_joke()
            case '2':
                print_movies()
            case '3':
                select_game()
            case '4':
                print('Bye bye')
                break


if __name__ == '__main__':
    play_music_in_background()
    draw_menu()
