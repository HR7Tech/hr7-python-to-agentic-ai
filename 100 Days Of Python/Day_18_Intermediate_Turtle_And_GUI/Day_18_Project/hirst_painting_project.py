# colorgram module can extract dominant colors from an image.
# import colorgram

# Extract colors from an image
# colors = colorgram.extract('hirst painting.jpg', 40)  # 40 = number of colors to extract

# Convert colors to RGB tuples
# rgb_colors = []
# for color in colors:
#     rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rgb)

# print(rgb_colors)

from turtle import Turtle,Screen
import random

# List of colors without background color (white).
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), 
 (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), 
 (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), 
 (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), 
 (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), 
 (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

# ---------------------------
# Turtle setup
# ---------------------------
screen = Screen()
screen.colormode(255)
t = Turtle()
t.speed("fastest")
t.hideturtle()
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

# ---------------------------
# Hirst-style dot painting
# ---------------------------
for dot_count in range(1 , number_of_dots + 1):
    t.dot(20,random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen.exitonclick()