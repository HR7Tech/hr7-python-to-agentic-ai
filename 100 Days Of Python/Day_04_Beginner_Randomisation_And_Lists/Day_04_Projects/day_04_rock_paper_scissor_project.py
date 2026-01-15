import random
from day_04_designs_rock_paper_scissor_project import rock,paper,scissors

print("Welcome to Rock , Paper , Scissors.!")

choices = [rock,paper,scissors] # Imported from day_04 desings file..

# -------------------------------------------------

# User Input

user = int(input("Press '0' for rock , '1' for paper or '2' for scissors: "))
if user > 2 or user < 0:
    print("Invalid Input.")
else:
    print(f"Player chose:\n{choices[user]}")

# -------------------------------------------------

# Assigning a random value to the computer.

computer = random.randint(0,2)
print(f"Computer chose:\n{choices[computer]}")

# -------------------------------------------------

# Game Rules: 
# ROCK (0) BEATS SCISSORS (2)
# PAPER (1) BEATS ROCKS (0)
# SCISSORS (2) BEATS PAPER (1)

# -------------------------------------------------

# Game Logic:

# DRAW
if user == computer:
    print("Draw")

# USER WINS
elif user == 0 and computer == 2:
    print("You Win.")
elif user == 1 and computer == 0:
    print("You Win.")
elif user == 2 and computer == 1:
    print("You Win.")

# USER LOSE
elif computer == 0 and user == 2:
    print("You Lose.")
elif computer == 1 and user == 0:
    print("You Lose.")
elif computer == 2 and user == 1:
    print("You Lose.")

# INVALID INPUT = NO RESULT
else:
    print("No Result.")


