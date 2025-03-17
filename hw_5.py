from random import randint
from decouple import config

from termcolor import cprint
def find_number():
    user_guess = int(input('GUESS NUMBER (FROM 1 TO 100): '))

    min_number = config('MIN_NUMBER', default=1, cast=int)
    max_number = config('MAX_NUMBER', default=100, cast=int)
    attempts = config('ATTEMPTS',default=2, cast=int)
    bonus = config('BONUS',default=500, cast=int)

    number = randint(min_number, max_number)
    while attempts > 0:
        if user_guess == number:
            bonus *= 2
            attempts -= 1
            return f'You won: {user_guess} attempts: {attempts} bonus: {bonus}'


        else:
            bonus -= 500
            attempts -= 1
            if attempts == 0:
                return (f'You lost! the number was: {number} \nattempts left: {attempts} '
                    f'\nbonus: {bonus}')
            else:
                user_guess = int(input(f'Wrong guess! You have {attempts} attempts left. Guess again: '))


cprint(find_number(), 'red', 'on_cyan')