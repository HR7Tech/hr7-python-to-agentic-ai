from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard
from food import Food
import time

screen = Screen()

# Setting Up Screen
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Turns off the screen until screen.update is called

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_on = False
        # scoreboard.game_over()
        scoreboard.reset_score()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_on = False
            # scoreboard.game_over()
            scoreboard.reset_score()
            snake.reset()



screen.exitonclick()

