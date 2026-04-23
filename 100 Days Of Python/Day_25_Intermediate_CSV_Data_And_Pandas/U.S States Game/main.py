import turtle
import pandas as pd

# Screen Setup
screen = turtle.Screen()
screen.title("U.S States")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading Data
data = pd.read_csv("50_states.csv")
all_states = data["state"].str.title().tolist()
guessed_states = []

# Turtle Writing Setup
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Game Logic

while len(guessed_states) < 50:

    answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Name a U.S. State (or type 'Exit' to quit):"
    )

    if answer is None: # User Closed The Dialogue
        break

    answer = answer.strip().title()

    if answer == "Exit":
        #Save missed states to CSV
        missed = [s for s in all_states if s not in guessed_states]
        missed_df = pd.DataFrame({"Missed States": missed})
        missed_df.to_csv("states_to_learn.csv")
        print("Saved missed states to states_to_learn.csv")
        break

    elif answer in all_states and answer not in guessed_states:
        screen.title("U.S States")
        guessed_states.append(answer)

        # Writer (Turtle) Writes The Answer To The Given Position
        row = data[data["state"].str.title() == answer]
        x = row["x"].values[0]
        y = row["y"].values[0]

        writer.goto(x,y)
        writer.write(answer,align="center",font=("Arial", 7, "bold"))

    elif answer in guessed_states:
        screen.title(f"Already Guessed {answer}! Try another state.")

    elif answer not in guessed_states and answer not in all_states:
        screen.title(f"{answer} is not a U.S State! Try another state.")

