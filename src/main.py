# Standard library imports
import os
import csv
import random
from datetime import datetime


# Related third-party imports
from colored import Fore, Back, Style # type:ignore
from prettytable import PrettyTable # type:ignore
from datetime import datetime

# Local application/library specific
from functions import clear_terminal, exit_game

# Hangman ASCII art: representing different stages of the game
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

# Class representing the Hangman game
class Hangman:
    def __init__(self, word):
        self.word = word.upper()
        self.guesses_left = len(HANGMAN) - 1
        self.guessed_letters = set()
        self.current_progress = ['_' if letter.isalpha() else letter for letter in self.word]
        self.hangman_stage = 0

    # Method to make a guess
    def guess(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            clear_terminal()
            print(f"\n{Fore.RED}You've already guessed that letter!{Style.RESET}")
            return

        self.guessed_letters.add(letter)

        if letter in self.word:
            clear_terminal()
            print(f"\n{Fore.GREEN}CORRECT!{Style.RESET}")
            for i, char in enumerate(self.word):
                if char == letter:
                    self.current_progress[i] = letter
        elif not letter.isalpha():
            clear_terminal()
            print(f"\n{Fore.RED}That's not a letter! Try again!{Style.RESET}")
        elif len(letter) > 1:
            clear_terminal()
            print(f"\n{Fore.RED}One guess at a time please! Try again!{Style.RESET}")
        else:
            clear_terminal()
            print(f"{Fore.RED}INCORRECT!{Style.RESET}")
            self.guesses_left -= 1
            self.hangman_stage += 1

# Method to update the current progress of game
    def update_progress(self):
        print(' '.join(self.current_progress))
        print("\nLetters guessed:", ', '.join(sorted(self.guessed_letters))) 
        print(HANGMAN[self.hangman_stage])

# Method to check whether user has lost or won game
    def game_over(self):
        if '_' not in self.current_progress:
            clear_terminal()
            print("*************************************")
            print(f"{Fore.WHITE}{Back.GREEN}\n!!!  YOU WON  !!!\n\nCongratulations!\n{Style.RESET}")
            print("*************************************\n")
            add_to_scoreboard(True)
            reset()
            return True
        elif self.guesses_left == 0:
            clear_terminal()
            print(f"{Fore.WHITE}{Back.RED}!!!  YOU LOSE  !!!{Style.RESET}\n")
            print(HANGMAN[7])
            print(f"{Fore.WHITE}{Back.RED}\nBetter luck next time, bucko.{Style.RESET}")
            print(f"{Fore.WHITE}{Back.RED}\nThe correct word was: {self.word}{Style.RESET}\n")
            add_to_scoreboard(False)
            reset()
            return True
        return False
    
# Function to add game result to the scoreboard
def add_to_scoreboard(won):
    try:
        with open("scoreboard.csv", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = "WON" if won else "LOST"
            f.write(f"{timestamp},{result}\n")
    except IOError as e:
        print(f"\n{Fore.RED}Error writing to scoreboard file: {e}{Style.RESET}")


# Display scoreboard with dates recorded
def display_scoreboard():
        clear_terminal()

        while True:
            try:
                with open("scoreboard.csv", "r") as f:
                    scores = f.readlines()
                    if len(scores) > 1:
                        
                        print(f"\n{Fore.CYAN}       ~~ SCOREBOARD ~~\n{Style.RESET}")
                        # Create a PrettyTable object with the column names
                        table = PrettyTable(["DATE", "SCORE"])
                        for idx, score in enumerate(scores):
                            if idx == 0:  # Skip the first line (header)
                                continue
                            score_data = score.strip().split(',')
                            if len(score_data) == 2:
                                name, score = score.strip().split(',')
                                table.add_row([name, score])
                        print(table)
                    else:
                        print(f"\n{Fore.RED}Scoreboard is empty. Start playing to track your score!{Style.RESET}")

                    response = input(F"\n{Fore.GREEN}Press 'M' to return to the main menu or 'Q' to quit the scoreboard: {Style.RESET}")
                    if response.lower() == 'm':
                        main_menu()
                    elif response.lower() == 'q':
                        exit_game()
                    else:
                        clear_terminal()
                        print(f"\n{Fore.RED}Invalid input. Please try again.{Style.RESET}")
                    
            except FileNotFoundError:
                print(f"\n{Fore.RED}Scoreboard file not found.{Style.RESET}")
            except IOError as e:
                print(f"\n{Fore.RED}Error reading scoreboard file: {e}{Style.RESET}")
    

# Function to get a random word from a list
def get_random_word(category):
    filename = f"{category}.txt"
    try:
        with open(filename, 'r') as file:
            word_list = [line.strip() for line in file]
        return random.choice(word_list)
    except FileNotFoundError:
        print(f"\n{Fore.RED}File '{filename}' not found.{Style.RESET}")
        return None
    except IOError as e:
        print(f"\n{Fore.RED}Error reading file: {e}{Style.RESET}")
        return None


# Main menu function
def main_menu():
    clear_terminal()
    print(f"\n{Back.BLUE_VIOLET}~~~ LET'S PLAY HANGMAN! ~~~{Style.RESET}\n")
    print("=================================\n")
    print(f"{Fore.BLUE_VIOLET}Enter [1] to START GAME{Style.RESET}")
    print(f"{Fore.BLUE_VIOLET}Enter [2] for GAME RULES{Style.RESET}")
    print(f"{Fore.BLUE_VIOLET}Enter [3] to DISPLAY SCOREBOARD{Style.RESET}")
    print(f"{Fore.BLUE_VIOLET}Enter [4] to EXIT{Style.RESET}")
    
    while True:
        menu_choice = input("\nSELECT AN OPTION: ")

        if menu_choice == "1":
            clear_terminal()
            game_start()
        elif menu_choice == "2":
            clear_terminal()
            game_help()
        elif menu_choice == "3":
            display_scoreboard()
        elif menu_choice == "4":
            clear_terminal()
            exit_game()
        else:
            print(f"\n{Fore.RED}Invalid option, please try again.{Style.RESET}")


# Game instructions
def game_help():
    print("HOW TO PLAY HANGMAN\n\n")
    print("Select a category from which you would like your hidden word to be selected")
    print("\nThe hidden word you are presented will be represented by underscores. Each underscore will represent a letter.\nThe player will receive 7 guesses to guess each letter individually.")
    print("\nEach correct letter guessed will replace the corresponding underscore, allowing the player to see where this\nletter resides in relation to the other letters within the hidden word")
    print("\nHOWEVER, if the player guesses incorrectly, they will see the hangman drawing progress to the next stage and lose on of their lives")
    print("\nShould the player lose all of their lives, they will have killed the hangman and trigger GAME OVER.")
    print("\nShould the player correct all of the letters correctly before the hangman dies, they will WIN.\n")

    while True:
        try:
            response = input(F"\n{Fore.GREEN}Press 'M' to return to the main menu{Style.RESET}")
            if response.lower() == 'm':
                main_menu()
            else:
                raise ValueError
        except ValueError:
            print(f"\n{Fore.RED}Invalid option, please try again.{Style.RESET}")



# Function to start the game
def game_start():
    categories = {
        1: "SPOOKY",
        2: "GEOGRAPHY",
        3: "VIDEO_GAMES",
        4: "MYTHOLOGY",
        5: "CULINARY_DELIGHTS",
    }

    print(f"\n{Back.BLUE_VIOLET}CATEGORIES:{Style.RESET}\n")
    for num, category in categories.items():
        print(f"{num}. {category}")
    
    while True:
        try:
            category_choice = int(input(f"\nEnter a {Fore.MAGENTA}number{Style.RESET} to select a category: "))
            selected_category = categories.get(category_choice)

            if selected_category:
                clear_terminal()
                print(f"You've selected the {Fore.MAGENTA}{selected_category}{Style.RESET} category!\n")
                word = get_random_word(selected_category)
                if word is None:
                    print(f"\n{Fore.RED}Failed to retrieve word. Please try again.{Style.RESET}")
                    continue
                game = Hangman(word)

                while not game.game_over():
                    print(f"\nRemaining guesses: {game.guesses_left}\n")
                    game.update_progress()
                    guess = input("Guess a letter: ")

                    if guess.strip() == "":
                        clear_terminal()
                        print(f"\n{Fore.RED}Invalid guess! Try again!{Style.RESET}")
                    else:
                        game.guess(guess)
                break
            else:
                print(f"\n{Fore.RED}Invalid category choice. Please select a valid category.{Style.RESET}")
        except ValueError:
            print(f"\n{Fore.RED}Invalid category choice. Please select a valid category.{Style.RESET}")

# Function to reset game
def reset():
    while True:
        try:
            options = input("Enter 'P' to PLAY AGAIN\nEnter 'S' to VIEW SCOREBOARD\nEnter 'Q' to QUIT GAME")
            reset = options.upper()
            if reset == "P":
                clear_terminal()
                game_start()
            elif reset == "S":
                display_scoreboard()
            elif reset == "Q":
                clear_terminal()
                print("Thanks for playing!\n\nSEEYA NEXT TIME\n")
                exit()
            else:
                clear_terminal()
                print(f"\n{Fore.RED}Invalid option, please try again.{Style.RESET}")
        except Exception as e:
            print(f"\n{Fore.RED}Error: {e}{Style.RESET}")


if __name__ == "__main__":
    main_menu()



# Current issues:
# {Fore.white} not working???
# Ensure that the program doesn't break if csv file is empty (have it start at 0,0)



