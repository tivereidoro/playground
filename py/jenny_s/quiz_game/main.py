#!/usr/bin/python3
from questions import questions_db

print("\n###### WELCOME TO QUIZ GAME ######\n")
print("#######################################\n")

# Score
number_of_questions = len(questions_db)
right_answers = 0

# Loop through questions
for question in questions_db:
    print(question["question"])
    print(question["options"])
    print()
    user_answer = input("Your answer: ").upper()

    q_count = questions_db.index(question) + 1
    
    if user_answer == question["answer"]:
        right_answers += 1
        print("Correct! Way to go!\n")
    else:
        print("You got that wrong!")
        print(f"The correct answer is: {question['answer']}\n")

    print(f"Your current score is: {right_answers}/{q_count}\n")


print("#########################################\n")
print("###### That's the end of the quiz! ######\n")
# Final score
print(f"You got {right_answers} question(s) right out of {number_of_questions}\n")
print(f"Your final score is: {right_answers / number_of_questions * 100}%\n")


