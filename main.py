# System packages
import os.path
import random

# External packages

# Imports of custom functions
from functions import theme_menu, welcome, game_over, user_guess, clear_terminal, read_file

# Start game --> choose catergory menu
welcome()
    
choice = ""

while choice != "6":
    choice = theme_menu()

    if (choice == "1"):
        game_word = read_file("spooky.txt")
        user_guess()
    elif (choice == "2"):
        game_word  = read_file("geography.txt")
        user_guess()
    elif (choice == "3"):
        game_word = read_file("video.txt")
        user_guess()
    elif (choice == "4"):
        game_word = read_file("myth.txt")
        user_guess()
    elif (choice == "5"):
        game_word = read_file("food.txt")
        user_guess()
    elif (choice == "6"):
        print("You've exited the program. Goodbye!")
        break
    else:
        print("Please choose from the option list provided")


game_over = False

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
 / \\       |
            |
            |
            |
===============
''','''
  +---------+
  |         |
  O         |
 /|\\       |
  |         |
            |
            |
===============
''','''
  +---------+
  |         |
  O         |
 /|\\       |
  |         |
 /          |
            |
===============
''','''
  +---------+
  |         |
  O         |
 /|\\       |
  |         |
 / \\       |
            |
===============
'''
]


