#!/usr/bin/python3
import random as ran
from hangman_diagram import stages
from word_list import words

# Welcome et instructions
print("\n🤗 Welcome to the HangMan Game 🚀🚀.\n")
# Init the number of lives and game 0ver for while loop exit
lives = 6
game_over = False
# Pick random word from list
random_word = ran.choice(words)
print(f"A random {len(random_word)}-letter word has been generated..")
print(f"Guess the word one letter at a time.\nYou have {lives} chances.\n")

# Show the blank display of the word
display = []
for _ in random_word:
    display += '_'
print(f"{display}\n")

while not game_over:
    guessed_letter = input("Guess a letter : ").lower()

    for position in range(len(random_word)):
        if random_word[position] == guessed_letter:
            display[position] = guessed_letter
            print("\nCorrect.! Way to go..🎯\n")
    print(display)

    if guessed_letter not in random_word:
        lives -= 1
        print("\n❌ Try again. ♻")
        if lives == 0:
            game_over = True
            print("\n❌ You ran out of chances.. Game Over.!!")

    if '_' not in display:
        game_over = True
        print(f"\nExcellent. You guessed the right word - {random_word.capitalize()}\n")
        print("🎉 🎉 🎉\n🏆 🏆 🏆\n🥇 🥇 🥇")

    print(stages[lives])
    print(f"❗❗ You have {lives} chances left ⚠.\n")
