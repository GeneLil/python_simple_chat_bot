"""Module with silly jokes"""
import pyjokes


def tell_a_joke():
    """Tell a joke"""
    print(pyjokes.get_joke('en', category='all'))
    