"""Chat bot"""
import random
import typing
import pyjokes
from prettytable import PrettyTable
from script_background_music import play_music_in_background


action_movies = {
    'Die Hard': '1998',
    'Aliens': '1986',
    'Seven Samurai': '1954',
    'The Wild Bunch': '1969',
    'Police Story': '1985',
    'Enter the Dragon': '1973',
    'Mad Max 2: The Road Warrior': '1981'
}

horror_movies = {
    'The Exorcist': '1973',
    'Hereditary': '2018',
    'The Conjuring': '2013',
    'The Shining': '1980',
    'The Texas Chainsaw Massacre': '1974',
    'The Ring': '2002',
    'Halloween': '1978',
    'Sinister': '2012',
    'Insidious': '2010'
}


def tell_a_joke():
    """Tell a joke"""
    print(pyjokes.get_joke('en', category='all'))


def draw_pretty_table(cols: typing.List[str], rows: typing.Dict):
    """Prettify data in the table"""
    pretty_table = PrettyTable()
    pretty_table.field_names = cols
    for row in rows:
        pretty_table.add_row([row, rows[row]])
    print(pretty_table)


def select_genre():
    """Selects genre"""
    print('Input genre: action | horror')
    return input()


def print_movies():
    """Prints movies"""
    genre = select_genre()
    movie_params = ['Movie name', 'Year']
    movies_to_print = {}
    match genre:
        case 'action':
            movies_to_print = action_movies
        case 'horror':
            movies_to_print = horror_movies
    print(f'Here\'s a list of best movies in {genre} genre')
    draw_pretty_table(movie_params, movies_to_print)


def main_menu_choice():
    """Draws main menu"""
    return input('''
Menu:
1. Tell a joke to start the day!
2. Recommend a movie.
3. Play a game.
4. Exit
''')


def rock_paper_scissors():
    """Classic game to play in schools"""
    user_choices = {
        '1': 'rock',
        '2': 'paper',
        '3': 'scissors'
    }
    pc_choices = ['rock', 'paper', 'scissors']
    user_score = 0
    pc_score = 0
    win_score = 3


    def user_won_round():
        nonlocal user_score
        print('You won this round!')
        user_score += 1

    def pc_won_round():
        nonlocal pc_score
        print('You lost this round!')
        pc_score += 1


    def print_current_score():
        print('\nCurrent score:')
        print('You:', user_score, 'PC:', pc_score, '\n')


    def check_result():
        nonlocal user_score
        nonlocal pc_score
        result = ''

        if user_score == win_score:
            print('Congrats! You have won!')
            result = 'end'
        if pc_score == win_score:
            print('You lost! Oh no...')
            result = 'end'
        return result

    while True:
        pc_choice = random.choice(pc_choices)
        user_choice_key = input('''
Action:
1. Rock
2. Paper
3. Scissors
4. Exit game
''').lower()

        if user_choice_key == '4':
            break

        if user_choice_key not in user_choices:
            print('Wrong value, try again!')
            continue

        user_choice = user_choices[user_choice_key]
        print('\nYou:', user_choice, 'PC:', pc_choice)
        winning_conditions = dict({
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper',
        })

        if user_choice == pc_choice:
            print('\nA draw. Try again!')
            print_current_score()
            continue

        for key, value in winning_conditions.items():
            if user_choice == key and pc_choice == value:
                user_won_round()
                break
        else:
            pc_won_round()

        print_current_score()
        if check_result() == 'end':
            break


def guess_the_number():
    """Play Guess the Number"""
    random_number = round(random.random() * 100)
    tries = 0
    while True:
        users_num = input('Enter the guess: ')

        if not users_num.isdigit():
            print('Entered wrong symbol, try again!')
            continue

        diff = abs(random_number - int(users_num))
        if diff >= 100:
            print('So cold! Try again!')
            tries += 1
        elif diff >= 50:
            print('Nice guess, but still cold!')
            tries += 1
        elif 50 > diff >= 20:
            print('It\'s getting warmer!')
            tries += 1
        elif 20 > diff >= 10:
            print('It is getting hotter now!')
            tries += 1
        elif 10 > diff >= 5:
            print('It is very hot!')
            tries += 1
        elif 5 > diff >= 1:
            print('It is hell!')
            tries += 1
        elif diff == 0:
            print(f'You have won with {tries} tries!')
            break


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
