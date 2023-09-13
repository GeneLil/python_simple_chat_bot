"""Rock paper scissors module"""
import random


def rock_paper_scissors():
    """Classic game"""
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
