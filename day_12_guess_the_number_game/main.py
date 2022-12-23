from art import logo
from random import *
print(logo)

print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100')
number_to_guess = randint(1, 100)
print(f'Psst correct number is {number_to_guess}')
choose_game_level = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()

game_level = None

if choose_game_level == 'easy':
    game_level = 10
else:
    game_level = 5


def check_the_answer(make_guess, number_to_guess, game_level):
    if make_guess == number_to_guess:
        print(f'You got it! The answer was {number_to_guess}')
        exit()
    elif make_guess > number_to_guess:
        game_level -= 1
        print('Too high.')
        print('Guess again')
    elif make_guess < number_to_guess:
        game_level -= 1
        print('Too low.')
        print('Guess again')


while game_level > 0:
    print(f'You have {game_level} attempts remaining to gouess the number')
    make_guess = int(input('Make a guess: '))
    if game_level == 1 and make_guess != number_to_guess:
        if make_guess > number_to_guess:
            game_level -= 1
            print('Too high.')
        elif make_guess < number_to_guess:
            game_level -= 1
            print('Too low.')
        print('You\'ve run out of guess, you loose')
    else:
        if make_guess == number_to_guess:
            print(f'You got it! The answer was {number_to_guess}')
            break
        elif make_guess > number_to_guess:
            game_level -= 1
            print('Too high.')
            print('Guess again')
        elif make_guess < number_to_guess:
            game_level -= 1
            print('Too low.')
            print('Guess again')


