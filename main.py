# System packages
import random
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

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

class Hangman:
    def __init__(self, word):
        self.word = word.upper()
        self.guesses_left = len(HANGMAN) - 1
        self.guessed_letters = set()
        self.current_progress = ['_' if letter.isalpha() else letter for letter in self.word]
        self.hangman_stage = 0

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            print("You've already guessed that letter! Try again!")
        else:
            print("INCORRECT")
            guesses_left -= 1
            hangman_stage += 1




def find_random_word(category):
    filename = f"{category}.txt"
    with open(filename, "r") as f:
        word_list = [f.read().splitlines()]
    return random.choice(word_list)

def game_start():
    categories = {
        1: "SPOOKY",
        2: "GEOGRAPHY",
        3: "VIDEO_GAMES",
        4: "MYTHOLOGY",
        5: "CULINARY_DELIGHTS"
    }

    print("\nCATEGORIES:\n")
    for num, category in categories.items():
        print(f"{num}. {category}")
    
    choose_category = int(input("\nEnter the number to select a category: "))
    selected_category = categories.get(choose_category)

    if selected_category:
        clear_terminal()
        print(f"You've selected the {category} category!\n")
        word = find_random_word(selected_category)
        game = Hangman(word)

        while not game.is_game_over():
            print(f"\nRemaining guesses: {game.guesses_left}")
            game.display_progress()
            guess = input("Guess a letter: ")
            game.guess(guess)
    else:
        print("Invalid category choice. Please select a valid category.")

if __name__ == "__main__":
    game_start()