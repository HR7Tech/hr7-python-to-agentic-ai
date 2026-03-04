from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()

# Setting Up Screen
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Turns off the screen until screen.update is called

snake = Snake()
screen.listen()

screen.onkey(fun = snake.up,key = "Up")
screen.onkey(fun = snake.down,key ="Down")
screen.onkey(fun = snake.right,key ="Right")
screen.onkey(fun = snake.left,key ="Left")

# Game Logic
game_on = True

while game_on:
    screen.update() # Updates the screen
    time.sleep(0.1) # Stops for 0.1 Second
    snake.move()


screen.exitonclick()