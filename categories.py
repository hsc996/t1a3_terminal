import random

def read_file(filename):
    try:
        with open(filename, "r") as f:
            words = f.read().splitlines()
            chosen_word = random.choice(words)
        return chosen_word
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
