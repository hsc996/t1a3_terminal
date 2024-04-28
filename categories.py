import random

def spooky():
    with open(f"spooky.txt", "r") as f:
        word = f.read().splitlines()
        chosen_word = random.choice(word)
    return chosen_word

def geography():
    with open(f"geography.txt", "r") as f:
        word = f.read().splitlines()
        chosen_word = random.choice(word)
    return chosen_word

def games():
    with open(f"video_games.txt", "r") as f:
        word = f.read().splitlines()
        chosen_word = random.choice(word)
    return chosen_word

def mythology():
    with open(f"mythology.txt", "r") as f:
        word = f.read().splitlines()
        chosen_word = random.choice(word)
    return chosen_word

def culinary():
    with open(f"culinary_delights", "r") as f:
        word = f.read().splitlines()
        chosen_word = random.choice(word)
    return chosen_word
