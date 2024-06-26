import os
from pyfiglet import Figlet # type:ignore
from colored import Fore, Back, Style # type:ignore

fig = Figlet(font='standard')

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def exit_game():
    clear_terminal()
    print(fig.renderText('SEEYA!'))
    print(f"{Fore.BLUE_VIOLET}Thanks for playing!{Style.RESET}\n\n")
    try:
        exit()
    except Exception as e:
        print(f"\n{Fore.RED}Error occurred while exiting: {e}{Style.RESET}")

def add_num(num1, num2):
    return num1 + num2

