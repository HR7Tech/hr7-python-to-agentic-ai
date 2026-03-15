import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Create cars and make them move from left to right of the screen
    car_manager.create_car()
    car_manager.move_cars()

    # Detect players collision with the car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # Detect level complete
    if player.level_complete():
        player.starting_position()
        car_manager.level_up()
        score.level_up()



screen.exitonclick()