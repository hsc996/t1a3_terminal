import os
from colored import Fore, Back, Style # type:ignore

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_game():
    print("\nSEEYA NEXT TIME!\n")
    try:
        exit()
    except Exception as e:
        print(f"\n{Fore.RED}Error occurred while exiting: {e}{Style.RESET}")
