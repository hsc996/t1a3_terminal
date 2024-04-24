def welcome():
    print(f"\nLet's Play Hangman!")
    print("\n=============================\n")

def theme_menu():
    print(f"1. SPOOKY")
    print(f"2. GEOGRAPHY")
    print(f"3. VIDEO GAMES")
    print(f"4. MYTHOLOGY")
    print(f"5. CULINARY DELIGHTS")
    print(f"6. EXIT GAME")

    user_choice = input("\nSelect your category: ")
    return user_choice