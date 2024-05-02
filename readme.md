## T1A3 TERMINAL APPLICATION

#### LINKS
Github repository: https://github.com/hsc996/t1a3_terminal

#### STYLE GUIDE: PEP8

_Imports:_
I've selected the PEP 8 style guide for python code, which I have adhered to throughout. According to the PEP8 styling guide, imports should be separated into 3 groups: standard library imports, related third party imports and local application imports. The style guide states that imports should be put "at the top of the file" and should be "on separate lines", making it easier to read and understand the dependencies of the script (Van Rossum et al., 2001). When viewing the code, one can see I have filed and labelled each import appropriately in accordance with these rules.

_Comments:_
I've used concise comments throughout to indicate the purpose of various classes, methods and functions. I've ensured they're all in complete sentences with the first word capitalised, as per the guildlines (Van Rossum et al., 2001). I've included these comments to enhance code readability and help other developers udnerstand the logic of the code.

_Whitespaces:_
The code has consistent whitespace around operators and after commas, making it easier to read and understand. Furthermore, each method in the Hangman class is separated by a single blank line, as recommended by PEP 8 (Van Rossum et al., 2001).

_Indentation:_
As outlined by the PEP 8 guidelines, I've ensured that my code follows the standard indentation style of using four spaces per level.

_Variable names:_
Variable names are descriptive and follow the recommended naming conventions. For example, HANGMAN is in all caps, indicating it's a constant, and Hangman is in CamelCase, indicating it's a class name. 

_Function and Method Names:_
All function and method names are descriptive, ensuring their functionality is clear to whomever is reading the code. Each function and method name adhere to the snake_case naming convention, which is the preferred convention outlined within the PEP 8 styleguide (Van Rossum et al., 2001). For example, main_menu, game_help, and game_start.

_String Formatting:_
I've used string formatting consistently throughout the code. For example, print(f"{Fore.RED}You've already guessed that letter!{Style.RESET}"). By consistently formatting all of the error messages in red, and the "CORRECT!" messages in green, I have improved readilbility of the code as well as for the player.


#### FEATURES

1)


2) MAIN MENU

As the application is run, the main_menu function is called, and the user is presented with a menu requesting them to 1) start game, 2) access help/instructions or 3) exit game. I've chosen to display this inital welcome message and menu script via a series of print("") statements. In order to ensure that the menu will remain on screen unless the user chooses to exit by selecting "3", I've utilised a while loop to serve as the primary control structure, as it will run infinitely as long as its condition remains True. The user input is prompted and collected via an input function, which I've stored in the menu_choice variable. The input is then evaluated in a series of if-elif-else statements to determine the appropriate action based on the chosen option. The if/elif options point to 3 valid options for the user to choose, each calling the appropriate corresponding function to direct them to their option. Lastly, I've included the "else" statement to account for errors, so that rather than breaking the code by selecting an invalid option, as error message is displayed that prompts the user to try again.


3) WORD SELECTION FROM CATEGORIES

Once the user has selected to start the game, the 'game_start' function is called and a list of categories will be displayed: the categories I've selected are SPOOKY, GEOGRAPHY, VIDEO GAMES, MYTHOLOGY and CULINARY DELIGHTS. The function begins by defining a dictionary named categories, where the keys are numerical indices and the values are strings representing different categories (e.g., "SPOOKY", "GEOGRAPHY"). The function then iterates over the categories dictionary using a for loop, displaying each category along with its corresponding index number. I've printed both the categories and the header in coloured formatting for aesthetic purposes.

Just as I did in the main_menu function, I've included a "while True" loop to encapsulate the if/else conditions to ensure that it will run indefinitely. Within the loop, it will then prompt the player to select their category using an input function that I've stored within the 'category_choice' variable. I've used the 'int' function to convert the user input into an integer to avoid a TypeError. It then attempts to retrieve the selected category from the categories dictionary using 'categories.get(category_choice)'. If the selected category is valid (i.e., exists in the dictionary), the loop continues; otherwise, an error message is displayed, prompting the player to select a valid category.

Once a valid category is selected, the function clears the terminal screen, prints a message confirming the selected category, and retrieves a random word from that category using the 'get_random_word' function. If the word retrieval is unsuccessful (i.e., word is None), an error message is displayed, and the loop continues to prompt the player to select a valid category. If a word is successfully retrieved, a new instance of the Hangman class is created with the selected word.

Within the game loop ('while not game.is_game_over()'), the player is prompted to guess a letter. The guessed letter is validated, and if it's valid, the game's guess method is called to process the guess. The game loop continues until the game is over (either the player wins or loses). If the game loop exits (either by winning, losing, or encountering an error), the outer while loop (while True) breaks, and the function execution ends.

<-- Incude logic behind exception handling here // do a once over to see whether the variable scope is addressed -->




## REFERENCES

Van Rossum, G., Warsaw, B. and Coghlan, A. (2001) PEP 8 – Style Guide for Python Code. Available at:
https://peps.python.org/pep-0008/ (Accessed: 25 April 2024).

