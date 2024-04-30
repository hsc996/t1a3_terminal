# RUN IN TERMINAL TO COMMENCE GAME:
# 1. chmod +x run.sh
# 2. ./run.sh

# System packages
import random
import os

# External packages
from colored import Fore, Back, Style # type:ignore

# Import custom functions
from generic_game_funcitions import game_help, high_score


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
            print(f"\n{Fore.RED}You've already guessed that letter!{Style.RESET}")
            return

        self.guessed_letters.add(letter)

        if letter in self.word:
            print(f"\n{Fore.GREEN}CORRECT!{Style.RESET}")
            for i, char in enumerate(self.word):
                if char == letter:
                    self.current_progress[i] = letter
        elif not letter.isalpha():
            print(f"\n{Fore.RED}That's not a letter! Try again!{Style.RESET}")
        elif len(letter) > 1:
            print(f"\n{Fore.RED}One guess at a time please! Try again!{Style.RESET}")
        else:
            print(f"{Fore.RED}INCORRECT!{Style.RESET}")
            self.guesses_left -= 1
            self.hangman_stage += 1

# Tracking letters guessed and displaying them on screen
    def display_progress(self):
        print(' '.join(self.current_progress))
        print("\nLetters guessed:", ', '.join(sorted(self.guessed_letters))) 
        print(HANGMAN[self.hangman_stage])

# GAME OVER - Function to indicate whether player has won or lost game
    def is_game_over(self):
        if '_' not in self.current_progress:
            clear_terminal()
            print("*************************************")
            print(f"{Fore.RED}{Back.GREEN}\n!!!  YOU WON  !!!\n\nCongratulations!\n{Style.RESET}")
            print("*************************************\n")
            reset()
            return True
        elif self.guesses_left == 0:
            clear_terminal()
            print(f"{Fore.GREEN}{Back.RED}!!!  GAME OVER  !!!{Style.RESET}\n")
            print(HANGMAN[7])
            print(f"{Fore.GREEN}{Back.RED}\nBetter luck next time, bucko.\nThe correct word was: {self.word}{Style.RESET}\n")
            reset()
            return True
        return False
    

# Function to get a random word from a list
def get_random_word(category):
    filename = f"{category}.txt"
    with open(filename, 'r') as file:
        word_list = [line.strip() for line in file]
    return random.choice(word_list)



def main_menu():
    print(f"\n{Back.BLUE}LET'S PLAY HANGMAN!{Style.RESET}\n")
    print("Enter 1 to play game")
    print("Enter 2 for game instructions")
    print("Enter 3 to exit game")
    
    menu_choice = input("\nSELECT AN OPTION: ")

    valid_choices = ["1", "2", "3", "4"]

    if menu_choice not in valid_choices:
        print(f"\n{Fore.RED}Invalid option, please try again.{Style.RESET}")
    elif menu_choice == "1":
        clear_terminal()
        game_start()
    elif menu_choice == "2":
        clear_terminal()
        game_help()
    elif menu_choice == "3":
        clear_terminal()
        high_score()
    elif menu_choice == "4":
        clear_terminal()
        print("\nSEEYA NEXT TIME!\n")
        exit()

        

# Main game function
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
    
    while True:
        try:
            category_choice = int(input("\nEnter a number to select a category: "))
            selected_category = categories.get(category_choice)

            if selected_category:
                clear_terminal()
                print(f"You've selected the {Fore.MAGENTA}{selected_category}{Style.RESET} category!\n")
                word = get_random_word(selected_category)
                game = Hangman(word)

                while not game.is_game_over():
                    print(f"\nYou have {game.guesses_left} guesses remaining\n")
                    game.display_progress()
                    guess = input("Guess a letter: ")

                    if guess.strip() == "":
                        print(f"\n{Fore.RED}Invalid guess! Try again!{Style.RESET}")
                    else:
                        game.guess(guess)
                break
            else:
                print(f"\n{Fore.RED}Invalid category choice. Please select a valid category.{Style.RESET}")
        except ValueError:
            print(f"\n{Fore.RED}Invalid input! Please enter a number.{Style.RESET}")

# Asks the player if they want to play again & resets game
def reset():
    while True:
        reset = input("Play again?\n\nY/N: ")
        play_again = reset.upper()
        if play_again == "Y":
            clear_terminal()
            game_start()
        elif play_again == "N":
            clear_terminal()
            print("Thanks for playing!\n\nSEEYA NEXT TIME\n")
            break
        else:
            print(f"\n{Fore.RED}Invalid option, please try again.{Style.RESET}")

        exit()


if __name__ == "__main__":
    main_menu()

# Current issues:
# {Fore.white} not working???
# Add option to exit program



