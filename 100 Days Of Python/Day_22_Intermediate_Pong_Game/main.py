from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()

# Setting Up Screen
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)



r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Ball Bounces
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        # Ball Bounces
        ball.bounce_x()

    # If a right paddle misses the ball, resart from the middle and move to opposite paddle.
    if ball.xcor() > 400:
            ball.restart() 
            scoreboard.l_point()

    # If a left paddle misses the ball, resart from the middle and move to opposite paddle.  
    if ball.xcor() < -400:
            ball.restart() 
            scoreboard.r_point() 





    
    




screen.exitonclick()