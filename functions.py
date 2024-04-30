import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_game():
    print("\nSEEYA NEXT TIME!\n")
    exit()