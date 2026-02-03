import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

# Option 01 : Creating Multiple Functions:

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Choosing a random number between 1 and 100.
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()



# Option 02 : Inside One Single function:

def number_guessing_game():
    print(logo)
    number_to_guess = random.randint(1,100)
    # print(f"Number to guess: {number_to_guess}")

    print("Welcome to the Number Guessing Game.!")

    print("I am thinking of a number between 1 and 100.\n")
    level = input("Choose a difficulty: Easy or Hard? ").lower()

    lives = 0
    game_over = False

    if level == "easy":
        lives = 10
        print(f"You have {lives} attempts remaining to guess the number.")
    elif level == "hard":
        lives = 5
        print(f"You have {lives} attempts remaining to guess the number.")
    else:
        print("***** Invalid Input. Game Over.! *****")
        game_over = True


    while not game_over:
        guess = int(input("\nGuess a number: "))

        if guess == number_to_guess:
            print("\n***** You guessed the correct number. You won.! *****\n")
            game_over = True

        elif guess > number_to_guess:
            print("Too high.!")
            lives -= 1
            print(f"\nYou have {lives} attempts remaining to guess the number.")
            if lives == 0:
                print("\n***** You Lose.! *****\n")
                game_over = True

        elif guess < number_to_guess:
            print("Too Low.!")
            lives -= 1
            print(f"\nYou have {lives} attempts remaining to guess the number.")
            if lives == 0:
                print("\n***** You Lose.! *****\n")
                game_over = True

    if input("Type 'y' to restart the game or type 'n' to exit: ").lower() == "y":
        print("\n" * 25)
        number_guessing_game()
    else:
        print("\n***** Good Bye.! *****")

number_guessing_game()
