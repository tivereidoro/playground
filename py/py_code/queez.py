#!/usr/bin/python3
import random

# Define a dictionary of quiz areas with their corresponding questions and answers
quiz_areas = {
    "General Knowledge": {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
        "What is the largest planet in our solar system?": "Jupiter",
    },
    "Science": {
        "What is the chemical symbol for water?": "H2O",
        "What planet is known as the Red Planet?": "Mars",
        "What gas do plants absorb from the atmosphere?": "Carbon Dioxide",
        "What force keeps us on the ground?": "Gravity",
    },
    "History": {
        "Who was the first President of the United States?": "George Washington",
        "In what year did the Titanic sink?": "1912",
        "Who discovered America?": "Christopher Columbus",
        "What wall was torn down in 1989?": "Berlin Wall",
    }
}

def get_random_question(questions):
    """Returns a random question from the questions dictionary."""
    return random.choice(list(questions.keys()))

def check_answer(question, answer, questions):
    """Checks if the provided answer is correct for the given question."""
    correct_answer = questions[question]
    return correct_answer.lower() == answer.lower()

def ask_question(question):
    """Asks the user a question and returns their answer."""
    return input(f"{question} ")

def play_quiz_game(questions):
    """Plays the quiz game."""
    score = 0
    for _ in range(len(questions)):
        question = get_random_question(questions)
        answer = ask_question(question)
        if check_answer(question, answer, questions):
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {questions[question]}.")
    print(f"Your final score is {score}/{len(questions)}")

def main():
    print("Choose a quiz area:")
    for i, area in enumerate(quiz_areas, 1):
        print(f"{i}. {area}")
    choice = int(input("Enter the number of your choice: ")) - 1
    quiz_area = list(quiz_areas.keys())[choice]
    questions = quiz_areas[quiz_area]
    print(f"\nStarting {quiz_area} quiz...\n")
    play_quiz_game(questions)

if __name__ == "__main__":
    main()
