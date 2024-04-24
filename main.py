# System packages
import os.path

# External packages

# Imports of custom functions
from categories import spooky, geography, video_games, mythology, food
from menu_functions import theme_menu, welcome

# Start game --> choose catergory menu
welcome()
    
choice = ""
spooky_file = "spooky.txt"

while choice != "6":
    choice = theme_menu()

    if (choice == "1"):
        spooky(spooky_file)
    elif (choice == "2"):
        geography()
    elif (choice == "3"):
        video_games()
    elif (choice == "4"):
        mythology()
    elif (choice == "5"):
        food()
    elif (choice == "6"):
        break
    else:
        print("Please choose from the option list provided")


print("You've exited the program. Goodbye!")
