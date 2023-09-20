"""Chat bot"""
from script_background_music import play_music_in_background
from modules.select_game import select_game
from modules.recommend_movie import print_movies
from modules.tell_a_joke import tell_a_joke
from modules.get_weather import get_weather


def main_menu_choice():
    """Draws main menu"""
    return input('''
Menu:
1. Tell a joke to start the day!
2. Recommend a movie.
3. Play a game.
4. Get weather
5.Exit
''')


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
                get_weather()
            case '5':
                print('Bye bye')
                break


if __name__ == '__main__':
    play_music_in_background()
    draw_menu()
