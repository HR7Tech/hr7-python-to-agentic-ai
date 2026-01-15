# Functions in Python:

# A function in Python is created using the def keyword followed by the function name, parentheses, 
# and a block of code to perform a specific task.

def my_function():
    print("Hello World.!")
    print("This is my first function.!")

# A function may contain a print statement inside its block, 
# but it will not execute or display any output until the function is called.

my_function() # Calling the function 

# ---------------------------------------------------

name = input("Enter your name: ")

def greet_hello():
    print(f"Hello {name}")

greet_hello()    

# ---------------------------------------------------


# While Loop in Python:

# A while loop repeatedly executes a block of code as long as a specified condition remains true.

num = 6

print(f"Value of num variable before loop: {num}")

while num > 0:
    print(num)
    num -= 1

print(f"Value of num variable after loop: {num}")    