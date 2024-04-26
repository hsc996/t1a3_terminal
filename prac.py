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

def read_file(filename):
    with open(filename, "r") as f:
        words = f.read().splitlines()
        chosen_word = random.choice(words)
    return chosen_word

def display_hangman(incorrect_guesses):
    print(HANGMAN[incorrect_guesses])

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_guess(guessed_letters):
    while True:
        guess = input("\nGuess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
        else:
            return guess

def update_hidden_word(game_word, hidden_word, guess):
    for i, letter in enumerate(game_word):
        if letter == guess:
            hidden_word[i] = guess
    return hidden_word

def play_hangman(file_name):
    game_word = read_file(file_name)
    incorrect_guesses = 0
    hidden_word = ['_'] * len(game_word)
    guessed_letters = []

    while True:
        clear_terminal()
        display_hangman(incorrect_guesses)
        print("Guessed Word:", ' '.join(hidden_word))

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in game_word:
            hidden_word = update_hidden_word(game_word, hidden_word, guess)
            if '_' not in hidden_word:
                clear_terminal()
                print("CONGRATULATIONS!\n\nYou won!")
                break
        else:
            incorrect_guesses += 1
            if incorrect_guesses == 7:
                clear_terminal()
                print("\nYOU LOSE!\n\nThe correct word was:", game_word)
                break

    print("\n\nPlay again?\n\n")

# Main function to start the game
def main():
    clear_terminal()
    print("\nLet's Play Hangman!")
    print("\n=============================\n")

    while True:
        file_name = "words.txt"  # Adjust this to your filename
        play_hangman(file_name)

        play_again = input("Enter 'yes' to play again, or any other key to exit: ").lower()
        if play_again != 'yes':
            clear_terminal()
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()