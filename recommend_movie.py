"""Recomment movie module"""
import typing
from prettytable import PrettyTable
import pyjokes


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
