import os
import random


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


def user_guess(file_name):
    game_word = read_file(file_name)
    hidden_word = ['_'] * len(game_word)
    guessed_letters = []

    while game_over is not False:

        guess = input("\nGuess a letter: ")

        for i, letter in enumerate(game_word):
            if letter != '_' and guess == letter:
                hidden_word[i] = letter
        print(" ".join(hidden_word))

        if '_' not in hidden_word:
            clear_terminal()  # Check if no more underscores are left
            print("CONGRATUGLATIONS!\n\nYou won!")
            break

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