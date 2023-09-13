"""Guess the number module"""
import random


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