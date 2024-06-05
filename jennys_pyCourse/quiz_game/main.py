#!/usr/bin/python3

print("###### WELCOME TO YOUR QUIZ GAME ######")
print("#######################################")

# Questions
questions = ["What is the capital of France?", "What is the capital of Germany?", "What is the capital of Spain?"]
answers = ["Paris", "Berlin", "Madrid"]

# Score
score = 0

# Loop through questions
for question in questions:
    print(question)
    user_answer = input("Your answer: ")
    if user_answer in answers:
        print("Correct!")
        score += 1
    else:
        print("You got that wrong!")


