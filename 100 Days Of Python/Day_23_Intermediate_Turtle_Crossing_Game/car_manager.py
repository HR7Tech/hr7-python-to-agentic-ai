from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # This if statement slow down the number of cars created.
        random_chance = random.randint(1,6)
        if random_chance == 1:
          new_car = Turtle("square")
          new_car.shapesize(stretch_wid=1,stretch_len=2)
          new_car.penup()
          new_car.color(random.choice(COLORS))
          random_y = random.randint(-250,250) # Car will not generate at the starting and ending point
          new_car.goto(300,random_y) # Generate from right side of screen
          self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
