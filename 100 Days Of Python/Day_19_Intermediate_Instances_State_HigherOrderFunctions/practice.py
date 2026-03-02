from turtle import Turtle,Screen

tim = Turtle("turtle")
screen = Screen()

# Challenge : Make an Etch-A-Sketch App

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear():
    tim.reset()

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen() is a function which listens to the user input
screen.listen()

# screen.onkey(key,function) is a function which performs an action based on pressed key.!
screen.onkey(key = "w",fun = move_forward)
screen.onkey(key = "a",fun = move_left)
screen.onkey(key = "s",fun = move_backward)
screen.onkey(key = "d",fun = move_right)
screen.onkey(key = "c",fun = clear)

screen.exitonclick()