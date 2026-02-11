# Python Package Index
# https://pypi.org/

# Python turtle module documentation
# https://docs.python.org/3/library/turtle.html

from turtle import Turtle , Screen

jimmy = Turtle()
jimmy.color("gold","green")
jimmy.shape("turtle")
jimmy.forward(200)
jimmy.left(100)
jimmy.forward(200)
jimmy.left(100)
jimmy.forward(200)
jimmy.left(100)
jimmy.forward(200)

ui_screen = Screen()

# print(ui_screen.canvheight())
ui_screen.exitonclick()

# ------------------------------

# Prettytable documentation
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle" , "Charmander"])
table.add_column("Type",["Electric", "Water" , " Fire"])
table.align = "r"
print(table)



