# *** Lesson 1 : Describe The Problem ***

def my_function():
    for i in range(1, 20):
        print(i)
        if i == 20:
            print("You got it")


my_function()
# print(i)

# ---------------------------------------------------

# Describe the Problem - Write your answers as comments:

# ---------------------------------------------------

# Question # 1: What is the for loop doing?

# Answer # 1: The for loop will run 19 times and each time it will give its value to variable i.

# ---------------------------------------------------

# Question # 2: When is the function meant to print "You got it"?

# Answer # 2: The function here will not print "You got it" because it will only print this statement when i == 20.
# And for loop will run only till 19 because in range it's always like 
# range(starting (inclusive), ending (exclusive or n - 1))

# ---------------------------------------------------

# Question # 3: What are your assumptions about the value of i?

# Answer # 3: We can call it a temporary variable or local variable because we can only use
# it inside this for loop.!

# ---------------------------------------------------

# *** Lesson 2 : Reproduce The Bug ***

# Some bugs are sneaky, they only occur under certain conditions. 
# In order to debug them, we need to be able to reliably reproduce the bug 
# and diagnose our problem to figure out which conditions trigger the bug.

# Challenge 1: Change the code so that it always produces the occasional error.
# Challenge 2: Fix the code and remove the bug.

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = 6 # Challeng 1 Solution.
dice_num = randint(0, 5) # Challenge 2 Solution.


print(dice_images[dice_num])

# ---------------------------------------------------

# *** Lesson 3 : Play Computer ***

year = int(input("What's your year of birth? "))

# The condition to check with 1994 will never be executed 
# because the conditions below are checking whether the number
# is greater than 1994 or less than 1994 
# but there is no condition to check if number is equal to 1994. Same goes for 1980.!

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# ---------------------------------------------------

# Challenge : Play computer and go through the code line by line as 
# if you were executing the code to figure out why 1994 does not work as expected. 
# Then go ahead and fix the code.

# Solution:

# Year less than or equals to 1994 and Year greater than or equals to 1980 will be 'millennial'. 
# Above 1994 will be 'gen z'.
# Else they are 'boomer'.!

if year >= 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
else:
    print("You are a boomer.!")

# ---------------------------------------------------

# *** Lesson 4 : Fix The Errors ***

# We can use a try/except block in Python to catch any exceptions that might occur. 

# Example 1:

age = 0
try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid Input. Please give a numerical value.!")
    try:
        age = int(input("How old are you?"))
    except ValueError:
        print("Invalid Input again.!")

if age > 18:
    print(f"You can drive at age {age}.")

# ---------------------------------------------------

# Example 2:

try:
    print(6 > "five")
except TypeError:
    print("You can't mix integers and strings in a comparison")

# ---------------------------------------------------

# *** Lesson 5 : Use Print ***

# print() is our friend. It can help expose hidden values while our code is running.

word_per_page = 0
# print(word_per_page)

pages = int(input("Number of pages: "))
# print(pages)

word_per_page = int(input("Number of words per page: "))
# print(word_per_page)

total_words = pages * word_per_page
# print(total_words)


print(word_per_page == int(input("Number of words per page: ")))

# ---------------------------------------------------

# Lesson 5 : Use a Debugger

# Most IDEs (Intelligent Development Environments) will have built-in tools for debugging. 
# This is normally known as the debugger. In many ways, they are like print statements on steroids.

# Debuggers allows us to peek into our code during execution and 
# pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

# ---------------------------------------------------

