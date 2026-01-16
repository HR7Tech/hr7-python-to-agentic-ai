# HURDLE 04:

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# -------------------------------------------------

# The solution for Hurdle 4 can also be applied to Hurdle 1, Hurdle 2, and Hurdle 3.

# HURDLE 04 SOLUTION:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()    

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move() 