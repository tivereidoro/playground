# This is a simple game that allows you to guess a random number by the computer.

from random import randint
import sys


def guess_function(your_guess):
    """ This function allows you to guess the number. Takes your guess and generates a secret number for you to guess.  Yea,, I know. Just just have fun charley!!."""

    your_name = input(f"What's your name charley?: ")
    your_guess = int(input('Guess the secret number: '))

    random_number = randint(1, your_guess)
    

    if your_guess == random_number:
        print(f"Gbam!! You got it right charley.. Two bottles for you {your_name}.")
    else:
        print(f"You guessed wrong!! \ The correct guess would have been {random_number} but your guess was {your_guess}.")


guess_function(str(sys.argv[1]))
