# Using print function to print "Hello World".
print("Hello World!")

# -----------------------------------------------

# Challenge 1: Use \n to add another line of "Hello world".

# \n is an escape sequence character which adds a new line.
print("Hello world!\nHello world!\nHello world!")

# String concatenation:
print("Hello" + " Hamid")

# Challenge 2: Add a space between the strings
print("Hello" + " " + "Hamid")

# -----------------------------------------------

# input() function is used to collect user input and use it within your code.
print("My name is" + " " + "Hamid")
print("Hello " + input("What is your name? "))

# Challenge 3: Update the code to add an exclamation mark.
print("Hello " + input("What is your name? ") + "!")

# -----------------------------------------------

# len() function returns the number of items in an object
# (like a list, string, tuple, or dictionary).

# Challenge 4: Check the length of the user input.
print(len(input("What is your name?")))

# Challenge 5: Split everything into variables.

username = input("Enter your name: ")
length = len(username)

print(length)

# -----------------------------------------------

# The rules for naming a variable in Python:

# - Variable names can contain letters, numbers, and underscores (_).
# - Variable names must start with a letter or underscore, not a number.
# - Variable names cannot be a Python keyword (like for, if, class, etc.).
# - Variable names are case-sensitive (name ≠ Name).
# - Variable names should not contain spaces; use underscores instead (my_name).
# - Variable names should be descriptive for readability, but there’s no strict rule.

name = "Hamid"
length = len(name)
print(length)