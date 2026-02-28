'''
IMPORTANT
1. Each challenge is wrapped in its own code block.
2. Only one challenge should be uncommented at a time.
3. Uncomment the challenge you want to run and execute the file.
4. When done, comment it back before trying another challenge.
'''

from turtle import Turtle , Screen
import random

t = Turtle("turtle")
t.color("green", "yellow")

my_screen = Screen()

#######################################

# Challenge # 1 : Create a square.

# for _ in range(4):
#     t.forward(100)
#     t.right(90)

#######################################

# Challenge # 2 : Draw a Dashed Line (- - - - - - -)

# for _ in range(10):
#     t.forward(10)   # draw dash
#     t.penup()
#     t.forward(10)   # gap
#     t.pendown()

#######################################

# Challenge # 3 : Draw triangle , square , pentagon , hexagon ,
# heptagon , octagon , nonagon and decagon

# Note: Each shape should be of different pen color.!

# for sides in range(3, 11):  # 3 to 10 sides

    # generate random RGB color
    # r = random.randint(0,255)
    # g = random.randint(0,255)
    # b = random.randint(0,255)
    # t.pencolor(r, g, b) # pen color in tuple
    #
    # angle = 360 / sides # setting the direction to move turtle .
    #
    # for _ in range(sides):
    #     t.forward(80)
    #     t.right(angle)

#######################################

# Challenge # 4 : Generate a random walk.

# Note: Each time the Turtle moves , it should change its pen color.!

# directions = [0, 90, 180, 270]  # East, North, West, South
# t.width(10)
# t.speed("fastest")
# my_screen.colormode(255)
# for _ in range(50):  # number of steps
#     t.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255)) # Random pen color
#     t.setheading(random.choice(directions)) # Setting up the direction in which turtle will move.
#     t.forward(20)

#######################################

# Challenge # 5 : Draw a spirograph

# my_screen.colormode(255)
# t.speed("fastest")
#
# for _ in range(40): # Number of circles
#     t.pencolor(random.randint(0,255),
#                random.randint(0,255),
#                random.randint(0,255))
#     t.circle(100)
#     t.right(360 / 40)  # rotate a little for next circle

my_screen.exitonclick()