# Importing modules
import random
from words import word_list
from arts import logo , stages

# -------------------------------------------------

def hangmen_game():

    ### SETTING UP GAME: ###
    
    # Displaying the logo of the game from the variable of imported module art => logo
    print(logo)

    # Choosing a random word from the variable of imported module words => word_list
    chosen_word = random.choice(word_list)
    print(chosen_word)

    # Creating an empty placeholder for the "_'
    placeholder = ""

    # Inserting "_" inside the placeholder
    for _ in chosen_word:
        placeholder += "_"

    # Showing the number of "_" the chosen word has.!
    print(placeholder)

    # Setting users lives.
    lives = 6

    # Correct letter which user will guess will be stored inside correct_letters.
    correct_letters = []

    # Incorrect letter which user will guess will be stored inside incorrect_letters.
    incorrect_letters = []

    # Displaying user the number of lives left.!
    print(f"You have {lives}/6 lives remaining.!\n")

    # Displaying ascii art from the variable (LIST) of imported module art => stages
    print(stages[lives])

    # Creating a variable for the while loop.!
    game_over = False

# -------------------------------------------------

    # Game starts
    while not game_over:

        # -------------------------------------------------
        # GAMES LOGIC : 1/4

        # Reminding user the number of lives they have.!
        print(f"You have {lives}/6 lives remaining.!\n") 
        print(stages[lives])

        # Displaying correct and incorrect letters which user have guessed.!
        print(f"Correct Letters: {correct_letters}")
        print(f"Incorrect Letters: {incorrect_letters}\n")

        # User guesses the letter.!
        guess = input("Guess a letter: ").lower()

        # Checking if the correct guessed letter is already guessed by user.!
        if guess in correct_letters:
            print(f"You have already guessed this letter '{guess}'.!\n")

        # display shows the number of letters the user have to guessed.!
        display = ""

        # -------------------------------------------------
        # GAME LOGIC : 2/4

        # Running a loop on chosen_word to check if the guessed letter is correct or incorrect.!
        for letter in chosen_word: 

            if guess == letter:
                # If letter is correct the '_' of display will be changed to correct letter.
                display += letter 
                # Correct guessed letter added to correct_letters list.!
                correct_letters.append(letter) 

            elif letter in correct_letters: 
                # If correct guessed letter is in correct_letter's list then it will be displayed.
                display += letter

            else:
                # If the guessed letter is not in the chosen_word then at that loop point '_' will be added.
                display += "_" 

        print(f"Word to guess: {display}\n")

        # -------------------------------------------------
        # GAME LOGIC : 3/4

        # If all '_' are guessed correctly then user wins the game.!
        if "_" not in display: 
            print("You Win.!\n")

            # Asking if user wants to end the game or play again.!
            if input("Do you want to restart the game: yes or no ").lower() == "yes":
                hangmen_game() # Game Restarts.!
            else:
                game_over = True # Game Ends.!
                print("Good Bye.!") 
        
        # -------------------------------------------------
        # GAME LOGIC : 4/4

        # If the guessed letter is wrong and is not in the incorrect_letters list. 
        # The user will be warned about it and will not lose a life.
        if guess in incorrect_letters: 
            print(f"Be careful .! You have already chosen this letter '{guess}'.!\n")

        # If the guessed letter is wrong and is not in the incorrect_letters list 
        # then user will lose a life
        elif guess not in correct_letters: 

            # Incorrect guessed letter added to the incorrect_letters list
            incorrect_letters.append(guess) 
            print("Wrong letter. You lose a life.!\n")
            lives -= 1 # User loses a live.!

            # If user loses all of its lives then game will be over . User lose.!
            if lives == 0: 
                print("You lose.!\n")

                # Asking if user wants to end the game or play again.!
                if input("Do you want to restart the game: yes or no ").lower() == "yes":
                    hangmen_game() # Game Restarts.!
                else:
                    game_over = True # Game Ends.!
                    print("Good Bye.!") 

# -------------------------------------------------

hangmen_game() # Starting the Game.!

   