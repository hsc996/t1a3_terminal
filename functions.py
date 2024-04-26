import os
import random

HANGMAN = [
    f'''
  +---------+
            |
            |
            |
            |
            |
            |
===============
''','''
  +---------+
  |         |
            |
            |
            |
            |
            |
===============
''','''
  +---------+
  |         |
  O         |
            |
            |
            |
            |
===============
''','''
  +---------+
  |         |
  O         |
 /          |
            |
            |
            |
===============
''','''
  +---------+
  |         |
  O         |
 / \\        |
            |
            |
            |
===============
''','''
  +---------+
  |         |
  O         |
 /|\\        |
  |         |
            |
            |
===============
''','''
  +---------+
  |         |
  O         |
 /|\\        |
  |         |
 /          |
            |
===============
''','''
  +---------+
  |         |
  O         |
 /|\\        |
  |         |
 / \\        |
            |
===============
'''
]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    clear_terminal()
    print(f"\nLet's Play Hangman!")
    print("\n=============================\n")

def theme_menu():
    print(f"1. SPOOKY")
    print(f"2. GEOGRAPHY")
    print(f"3. VIDEO GAMES")
    print(f"4. MYTHOLOGY")
    print(f"5. CULINARY DELIGHTS")
    print(f"6. EXIT GAME")

    user_choice = input("\nSelect your category: ")
    return user_choice


def read_file(filename):
        with open(filename, "r") as f:
            words = f.read().splitlines()
            chosen_word = random.choice(words)
        return chosen_word

def display_hangman(incorrect_guesses):
    print(HANGMAN[incorrect_guesses])


def user_guess(file_name):
    game_word = read_file(file_name)
    incorrect_guesses = 0
    hidden_word = ['_'] * len(game_word)
    guessed_letters = []

    while True:  # Changed condition to True for the loop to be infinite unless broken explicitly
        guess = input("\nGuess a letter: ")

        if guess in game_word:  # Check if the guess is correct
            for i, letter in enumerate(game_word):
                if letter == guess:
                    hidden_word[i] = letter
        else:
            incorrect_guesses += 1  # Increment incorrect_guesses only if the guess is incorrect
            print(display_hangman(incorrect_guesses))
        
        print(" ".join(hidden_word))

        if '_' not in hidden_word:
            clear_terminal()  # Check if no more underscores are left
            print("CONGRATULATIONS!\n\nYou won!")
            print("\n\nPlay again?\n\n")
            break
        elif incorrect_guesses == 7:
            clear_terminal()
            print("\nYOU LOSE!\n\nThe correct word was:", game_word)
            print(HANGMAN[7] + "\n")
            print("\n\nPlay again?\n\n")
            break

        # Error handling 
        if guess == game_word:
            hidden_word = game_word
        elif not guess.isalpha() or len(guess) > 1:
            print(f'Invalid option, try again')
        elif guess in guessed_letters:
            print(f'Letter already guessed, try another.')
        else:
            guessed_letters.append(guess)
            guessed_letters.sort()


def game_over():
    pass
