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
    try:
        with open(filename, "r") as f:
            words = f.read().splitlines()
            chosen_word = random.choice(words)
        return chosen_word
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."


def user_guess():
    game_word = spooky()
    hidden_word = ['_'] * len(game_word)

    while game_over is not False:

        guess = input("Guess letter: ")

        for i, letter in enumerate(game_word):
            if letter != '_' and guess == letter:
                hidden_word[i] = letter

        print(" ".join(hidden_word))

def game_over():
    pass

        