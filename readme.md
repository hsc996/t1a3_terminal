## T1A3 TERMINAL APPLICATION

### LINKS
Github repository: https://github.com/hsc996/t1a3_terminal

### STYLE GUIDE: PEP8

#### _Imports:_
I've selected the PEP 8 style guide for python code, which I have adhered to throughout. According to the PEP8 styling guide, imports should be separated into 3 groups: standard library imports, related third party imports and local application imports. The style guide states that imports should be put "at the top of the file" and should be "on separate lines", making it easier to read and understand the dependencies of the script (Van Rossum et al., 2001). When viewing the code, one can see I have filed and labelled each import appropriately in accordance with these rules.

#### _Comments:_
I've used concise comments throughout to indicate the purpose of various classes, methods and functions. I've ensured they're all in complete sentences with the first word capitalised, as per the guildlines (Van Rossum et al., 2001). I've included these comments to enhance code readability and help other developers udnerstand the logic of the code.

#### _Whitespaces:_
The code has consistent whitespace around operators and after commas, making it easier to read and understand. Furthermore, each method in the Hangman class is separated by a single blank line, as recommended by PEP 8 (Van Rossum et al., 2001).

#### _Indentation:_
As outlined by the PEP 8 guidelines, I've ensured that my code follows the standard indentation style of using four spaces per level.

#### _Variable names:_
Variable names are descriptive and follow the recommended naming conventions. For example, HANGMAN is in all caps, indicating it's a constant, and Hangman is in CamelCase, indicating it's a class name. 

#### _Function and Method Names:_
All function and method names are descriptive, ensuring their functionality is clear to whomever is reading the code. Each function and method name adhere to the snake_case naming convention, which is the preferred convention outlined within the PEP 8 styleguide (Van Rossum et al., 2001). For example, main_menu, game_help, and game_start.

#### _String Formatting:_
I've used string formatting consistently throughout the code. For example, print(f"{Fore.RED}You've already guessed that letter!{Style.RESET}"). By consistently formatting all of the error messages in red, and the "CORRECT!" messages in green, I have improved readilbility of the code as well as for the player.


### FEATURES


1) MAIN MENU

As the application is run, the main_menu function is called, and the user is presented with a menu requesting them to 1) start game, 2) access help/instructions or 3) exit game. I've chosen to display this inital welcome message and menu script via a series of print("") statements. In order to ensure that the menu will remain on screen unless the user chooses to exit by selecting "3", I've utilised a while loop to serve as the primary control structure, as it will run infinitely as long as its condition remains True. The user input is prompted and collected via an input function, which I've stored in the menu_choice variable. The input is then evaluated in a series of if-elif-else statements to determine the appropriate action based on the chosen option. The if/elif options point to 3 valid options for the user to choose, each calling the appropriate corresponding function to direct them to their option. Lastly, I've included the "else" statement to account for errors, so that rather than breaking the code by selecting an invalid option, as error message is displayed that prompts the user to try again.


2) WORD SELECTION FROM CATEGORIES

Once the user has selected to start the game, the 'game_start' function is called and a list of categories will be displayed: the categories I've selected are SPOOKY, GEOGRAPHY, VIDEO GAMES, MYTHOLOGY and CULINARY DELIGHTS. The function begins by defining a dictionary named categories, where the keys are numerical indices and the values are strings representing different categories (e.g., "SPOOKY", "GEOGRAPHY"). The function then iterates over the categories dictionary using a for loop, displaying each category along with its corresponding index number. I've printed both the categories and the header in coloured formatting for aesthetic purposes.

Just as I did in the main_menu function, I've included a "while True" loop to encapsulate the if/else conditions to ensure that it will run indefinitely. Within the loop, it will then prompt the player to select their category using an input function that I've stored within the 'category_choice' variable. I've used the 'int' function to convert the user input into an integer to avoid a TypeError. It then attempts to retrieve the selected category from the categories dictionary using 'categories.get(category_choice)'. If the selected category is valid (i.e., exists in the dictionary), the loop continues; otherwise, an error message is displayed, prompting the player to select a valid category.

Once a valid category is selected, the function clears the terminal screen, prints a message confirming the selected category, and retrieves a random word from that category using the 'get_random_word' function. If the word retrieval is unsuccessful (i.e., word is None), an error message is displayed, and the loop continues to prompt the player to select a valid category. If a word is successfully retrieved, a new instance of the Hangman class is created with the selected word.

Within the game loop ('while not game.is_game_over()'), the player is prompted to guess a letter. The guessed letter is validated, and if it's valid, the game's guess method is called to process the guess. The game loop continues until the game is over (either the player wins or loses). If the game loop exits (either by winning, losing, or encountering an error), the outer while loop (while True) breaks, and the function execution ends.


3) WIN/LOSE TRIGGER

The 'game_over' method is responsible for triggering a final "game over" display at the end of the game, depending on the outcome. If the player corrects all the letters correctly within the frame of their allotted guesses, it will trigger a "YOU WON" display and if the player is unsuccessful, it will trigger a "YOU LOSE" display. This function is designed to work by calling to the Hangman class: the 'guess' method takes the letter as input and converts the letter to uppercase for consistency. If there are no underscores left in self.current_progress, it means the player has guessed all the letters correctly and won the game. If self.guesses_left becomes zero, it means the player has used all their chances and lost the game. In either case, the method prints a message informing the player of the outcome and resets the game. The game clears the terminal screen to keep the interface clean and readable after each guess. ASCII art representing the Hangman is displayed to provide a visual representation of the player's progress and the consequences of incorrect guesses.


<-- Include logic behind exception handling here // do a once over to see whether the variable scope is addressed -->

### Implementation Plan



### Project Management

#### Code Logic -- Flow Chart Algorithm

![flowchart](/src/assets/flowchart.jpg)

The flowchart above depicts an algorithm explaining the logic of the code. The "start" and "end" points are represented by the traditional oval shapes and have been colour coded for clarity. As there are a junctions within the code that depend on user input, I've use the paralellograms to incidicate the input/output points and colour coded them in purple. The burgundy rectangles represent a "process", while the teal diamond represent decision points in the code. There are some points in the code that are both decision points and require user input, in which I've decided to keep them as parallelograms.




### Help Documentation

#### _Considerations_

This application will execute a function that clears the terminal upon launch. It is recommended to launch this application in a separate window if you want to avoid losing any important data you may have in your terminal.

This applicaion has been designed and tested on a Macbook, however, should work on any system as long as Python 3 is installed.

#### _Dependencies_

In order to run this application, you must have Python 3 installed.

Below is a list of dependencies required for the app to run as intended:

colored==2.2.4
prettytable==3.10.0

These dependencies have been accounted for in the bash scripts, and will thus be included automatically upon launch.

#### _Installation_

This application will run from the "src" directory. Please ensure you are in correct directory before attempting to install.

If it is your first time using this application, you should run this command first:

"chmod +x run.sh"

Then, in order to run the app in your terminal, you must run command the "./run.sh".
If you've run this application before, "./run.sh" will be the only command required to run the application.









## REFERENCES

Van Rossum, G., Warsaw, B. and Coghlan, A. (2001) PEP 8 – Style Guide for Python Code. Available at:
https://peps.python.org/pep-0008/ (Accessed: 25 April 2024).

