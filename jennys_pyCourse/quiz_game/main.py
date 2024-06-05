#!/usr/bin/python3

print("\n###### WELCOME TO QUIZ GAME ######\n")
print("#######################################\n")

# Questions
# questions = ["What is the capital of France?", "What is the capital of Germany?", "What is the capital of Spain?"]
# answers = ["Paris", "Berlin", "Madrid"]

questions_db = [
    {"question": "What is the capital of France?",
     "options": "A. Paris\nB. New Jersey\nC. Berlin",
     "answer": "A"},
     
    {"question": "What is the capital of Germany?",
    "options": "A. Paris\nB. Berlin\nC. New Jersey",
    "answer": "B"},
]

# Score
score = 0

# Loop through questions
for question in questions_db:
    print(question["question"])
    print(question["options"])
    user_answer = input("Your answer: ").upper()
    
    if user_answer == question["answer"]:
        score += 1
        print(f"Correct! Your score is: {score}/2\n")
    else:
        print("You got that wrong!")
        print(f"The correct answer is: {question['answer']}\n")

# Final score
print(f"Your final score is: {score}/2\n")


