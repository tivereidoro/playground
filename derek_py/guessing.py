#!/usr/bin/python3


# Creating a guessing game
print("\nWelcome again pal, let's play.\n")
secret_number = 7

while True:
    try:
        guess = int(input("Guess a number tween 1 and 10 : "))

        if guess == secret_number:
            print("\nHurray!! You guessed the right number.\n")
            break
        else:
            print("\nNot quite right.. Try again!\n")
            continue

    except ValueError:
        print("\nOops, that's not a number. Type a number tween 1 and 10 : \n")
    except:
        print("\nAn unknown error occured.\n")
