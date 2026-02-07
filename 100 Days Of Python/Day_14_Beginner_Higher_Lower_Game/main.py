# Importing modules for this program
import random
from art import logo , vs
from game_data import data


# Created a function which provide output in formatted form.
def formatted_data(option):
    """This function take input and display's 'name' , 'description' and 'country' of generated option"""
    return f"{option['name']} , a {option["description"]} , {option["country"]}."

# Created a function which checks the answer user provided.
def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Game Logic
print(logo)
game_over = False
score = 0

option_b = random.choice(data)
while not game_over:
    # Generating two random options from the game data
    option_a = option_b
    option_b = random.choice(data)

    # If option_a and option_b are same it will regenerate another choice until they are different.
    while option_a == option_b:
        option_b = random.choice(data)

        

    print(f"Compare A: {formatted_data(option_a)}.")
    print(vs)
    print(f"Against B: {formatted_data(option_b)}.")    
    
    # Asking user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    # - Get follower count of each option.
    a_follower_count = option_a["follower_count"]
    b_follower_count = option_b["follower_count"]

    # Check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_over = True




