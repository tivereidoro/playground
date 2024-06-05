#!/usr/bin/python3

print("###### WELCOME TO QUIZ GAME ######\n")
print("#######################################\n")

# Questions
# questions = ["What is the capital of France?", "What is the capital of Germany?", "What is the capital of Spain?"]
# answers = ["Paris", "Berlin", "Madrid"]

questions_db = [
    {question: "What is the capital of France?",
     options: "A. Paris\nB. New Jersey\nC. Berlin",
     answer: "A"},
     {question: "What is the capital of Germany?", options: "A. Paris\nB. Berlin\nC. New Jersey", answer: "B"},
]

# Score
score = 0

# Loop through questions
for question in questions:
    print(question)
    user_answer = input("Your answer: ")
    
    if user_answer in answers:
        score += 1
        print("Correct!")
    else:
        print("You got that wrong!")


