enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}") # 2 ==>> Calling line 4 enemies variable

increase_enemies()
print(f"enemies outside function: {enemies}") # 1 ==>> Calling line 1 enemies variable

# ---------------------------------------------------

player_health = 2 # GLOBAL SCOPE

def game():
    def drink_potion():
        player_health = 20 # LOCAL SCOPE
        print(player_health)
    drink_potion()

game()
print(player_health)

# ---------------------------------------------------

# Exercise : Prime Number Checker

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

# ---------------------------------------------------

my_global_var = 1 # Accessible anywhere


def my_function():
    # Only accessible within my_function()
    my_local_var = 2


for _ in range(10):
    # Accessible anywhere
    my_block_var = 3

print(my_global_var) # 1

# print(my_local_var) # NameError

print(my_block_var) # 3

# ---------------------------------------------------

game_level = 3

enemies = ["zombie","skeleton","aliens"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # zombie

# ---------------------------------------------------

def create_enemy():
    if game_level < 5:
        another_enemy = enemies[0]

# print(another_enemy) # NameError

# ---------------------------------------------------

game_level = 5
game_level = 3
def create_enemy():
    # It's better to initialize a variable before updating/creating it inside the function. 
    # Because what if the condition is false then the variable will not be created/updated.
    # Then the function will print nothing.

    another_enemy = ""
    if game_level < 5:
        another_enemy = enemies[2]
    print(another_enemy)

create_enemy() # aliens

# ---------------------------------------------------

# Modifying Global Scope

enemies = 1


def increase_enemies():
    # This global keyword will now help us to update the global variable which is outside the functon.!
    global enemies 
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
increase_enemies()
increase_enemies()
print(f"enemies outside function: {enemies}")

# ---------------------------------------------------

# OR USE THE 'return' KEYWORD (MUCH PREFERRED)

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)

print(f"enemies outside function: {enemies}")

# ---------------------------------------------------

# CONSTANT variables are those variables which we will never ever change their values.

# More like 'set and forget'

# CONSTANT VARIABLES are usually written in capital letters .
# They can be updated if we want to but to make it
# different from other variables so that we will remember that 
# these variables should not be changed in the future.

PI = 3.14159

print(PI)

# Usually we create other variables with small letters and underscores.!

# So variables with all caps will seem strange, and 
# it will come to our mind oh this shouldn't be updated.!

# It's all upto us.! Remember we are programmers and the game is in our hands.!