from turtle import Turtle, Screen
import random

# ----------------------------
# Screen Setup
# ----------------------------
screen = Screen()
screen.setup(width = 500,height = 400)

# ----------------------------
# User Bet
# ----------------------------
user_bet = screen.textinput(title="Make a bet",
                            prompt="Which turtle will win the race: Enter a color ")

# ----------------------------
# Turtle Setup
# ----------------------------
color_list = ["red", "green", "blue", "yellow", "purple"]

turtles = []

for i in range(5):
    t = Turtle(shape="turtle")
    t.color(color_list[i])
    t.penup()
    t.goto(-230, -100 + i * 50)
    turtles.append(t)

# ----------------------------
# Race Logic
# ----------------------------

race_on = False

if user_bet in color_list:
    race_on = True

finish_line = 230   # right boundary for width=500

while race_on:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        # Check if this turtle crossed finish line
        if turtle.xcor() >= finish_line:
            race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won the race.")
            else:
                print(f"You lost! The {winning_color} turtle won the race.")

            break



screen.exitonclick()