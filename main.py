# System packages
import os.path
import random

# External packages

# Imports of custom functions
from functions import theme_menu, welcome, user_guess, clear_terminal, display_hangman

# Start game --> choose catergory menu
welcome()

# Game variables
game_over = False
game_win = False
game_word = None
game_stage = 0
total_lives = 7

def game_start():
    clear_terminal()
    print(f"\nYou've chosen the {category} category!\n")
          
    user_guess(f"{category}.txt")

choice = ""

while choice != "6":
    choice = theme_menu()
    valid_choices = ["1", "2", "3", "4", "5", "6"]

    if choice not in valid_choices:
        print("Invalid choice! Please select from the menu above")
    if (choice == "1"):
        category = "spooky"
        game_start()
    elif (choice == "2"):
        category = "geography"
        game_start()
    elif (choice == "3"):
        category = "games"
        game_start()
    elif (choice == "4"):
        category = "mythology"
        game_start()
    elif (choice == "5"):
        category = "food"
        game_start()
    elif (choice == "6"):
        print("You've exited the program. Goodbye!")
        break



