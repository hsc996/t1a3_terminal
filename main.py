# RUN IN TERMINAL TO COMMENCE GAME:
# 1. chmod +x run.sh
# 2. ./run.sh

# System packages
import random
import os

# External packages
from colored import Fore, Back, Style # type:ignore

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

HANGMAN = [
    '''
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
            print(f"\n{Fore.red}You've already guessed that letter!{Style.reset}")
            return

        self.guessed_letters.add(letter)

        if letter in self.word:
            print(f"\n{Fore.green}CORRECT!{Style.reset}")
            for i, char in enumerate(self.word):
                if char == letter:
                    self.current_progress[i] = letter
        elif not letter.isalpha() or len(letter) > 1:
            print(f"\n{Fore.red}Invalid guess! Try again!{Style.reset}")
        else:
            print(f"{Fore.red}INCORRECT!{Style.reset}")
            self.guesses_left -= 1
            self.hangman_stage += 1


    def display_progress(self):
        print(' '.join(self.current_progress))
        print("\nLetters guessed:", ', '.join(sorted(self.guessed_letters))) 
        print(HANGMAN[self.hangman_stage])

    def is_game_over(self):
        if '_' not in self.current_progress:
            clear_terminal()
            print("*************************************")
            print(f"{Fore.white}{Back.green}\n!!!  YOU WON  !!!\n\nCongratulations!\n{Style.reset}")
            print("*************************************")
            print("Play again? Y/N\n")
            return True
        elif self.guesses_left == 0:
            clear_terminal()
            print(f"{Fore.white}{Back.red}!!!  GAME OVER  !!!{Style.reset}\n")
            print(HANGMAN[7])
            print(f"{Fore.white}{Back.red}\nBetter luck next time, bucko.\nThe correct word was: {self.word}{Style.reset}\n")
            print("Play again? Y/N\n")
            return True
        return False

# Function to get a random word from a list
def get_random_word(category):
    filename = f"{category}.txt"
    with open(filename, 'r') as file:
        word_list = [line.strip() for line in file]
    return random.choice(word_list)

def game_start():
    categories = {
        1: "SPOOKY",
        2: "GEOGRAPHY",
        3: "VIDEO_GAMES",
        4: "MYTHOLOGY",
        5: "CULINARY_DELIGHTS"
    }

    print(f"\n{Back.blue}LET'S PLAY HANGMAN!{Style.reset}")
    print("\nCATEGORIES:\n")
    for num, category in categories.items():
        print(f"{num}. {category}")

    category_choice = int(input("\nEnter a number to select a category: "))
    selected_category = categories.get(category_choice)

    if selected_category:
        clear_terminal()
        print(f"You've selected the {selected_category} category!\n")
        word = get_random_word(selected_category)
        game = Hangman(word)

        while not game.is_game_over():
            print(f"\nYou have {game.guesses_left} guesses remaining\n")
            game.display_progress()
            guess = input("Guess a letter: ")

            if guess.strip() == "":
                print(f"\n{Fore.red}Invalid guess! Try again!{Style.reset}")
            else:
                game.guess(guess)
    else:
        print("Invalid category choice. Please select a valid category.")

if __name__ == "__main__":
    game_start()

# Current issues:
# Need to write reset function that allows user to play again
# Error handling to create error message when user selects invalid catgory
# Error handling - Enter button being taken as a correct guess
# {Fore.white} not working???


