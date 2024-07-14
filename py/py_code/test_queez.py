#!/usr/bin/python3
import pytest
from unittest.mock import patch
from queez import get_random_question, check_answer, ask_question, play_quiz_game, quiz_areas

def test_get_random_question():
    questions = quiz_areas["General Knowledge"]
    question = get_random_question(questions)
    assert question in questions

def test_check_answer_correct():
    questions = quiz_areas["General Knowledge"]
    question = "What is 2 + 2?"
    assert check_answer(question, "4", questions) == True

def test_check_answer_incorrect():
    questions = quiz_areas["General Knowledge"]
    question = "What is 2 + 2?"
    assert check_answer(question, "5", questions) == False

@patch('builtins.input', return_value='Paris')
def test_ask_question(mock_input):
    question = "What is the capital of France?"
    answer = ask_question(question)
    assert answer == 'Paris'

@patch('builtins.input', side_effect=['Paris', '4', 'Harper Lee', 'Jupiter'])
def test_play_quiz_game(mock_input, capsys):
    questions = quiz_areas["General Knowledge"]
    play_quiz_game(questions)
    captured = capsys.readouterr()
    assert "Correct!" in captured.out
    assert "Your final score is 4/4" in captured.out

if __name__ == "__main__":
    pytest.main()
