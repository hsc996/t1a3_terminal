import pytest
import os
from datetime import datetime

from main import Hangman, game_help, get_random_word


#Testing the Hangman class/methods
@pytest.fixture
def hangman_instance():
    # Example usage of the Hangman class
    word = "TEST"
    return Hangman(word)

# Test the initialization of Hangman
def test_hangman_initialization(hangman_instance):
    assert hangman_instance.word == "TEST"
    assert hangman_instance.guesses_left == 7  # Assuming HANGMAN is a list with 7 elements
    assert hangman_instance.guessed_letters == set()
    assert hangman_instance.current_progress == ['_', '_', '_', '_']
    assert hangman_instance.hangman_stage == 0

# Test the guess method
def test_hangman_guess(hangman_instance, capsys):
    # Test correct guess
    hangman_instance.guess('T')
    captured = capsys.readouterr()
    assert "CORRECT!" in captured.out

    # Test incorrect guess
    hangman_instance.guess('X')
    captured = capsys.readouterr()
    assert "INCORRECT!" in captured.out

    # Test already guessed letter
    hangman_instance.guess('T')
    captured = capsys.readouterr()
    assert "already guessed" in captured.out

    # Test non-letter guess
    hangman_instance.guess('1')
    captured = capsys.readouterr()
    assert "not a letter" in captured.out

    # Test multi-letter guess
    hangman_instance.guess('AB')
    captured = capsys.readouterr()
    assert "One guess at a time" in captured.out


# # Testing the game_help funciton + exception handling
class GameHelp:
    def test_game_help(capsys):
        # Capturing stdout to check printed output
        with capsys.disabled():
            game_help()  # Call the function

        # Capturing printed output
        captured = capsys.readouterr()

        # Expected output
        expected_output = """m"""

        # Asserting the printed output matches the expected output
        assert captured.out.strip() == expected_output.strip()

    def test_game_help():
        with pytest.raises(ValueError):
            game_help()

