# Strings: A string is a sequence of characters used to represent text,
# enclosed in single , double quotes or triple quotes in Python.

print(len("123"))
print(type("123"))

# ----------------------------------------------------------------

#  Challenge 1: Write "o" from "Hello".
print("Hello"[-1])
print("Hello"[4])

# ----------------------------------------------------------------

# Integers: An integer is a whole number (positive, negative, or zero) without any decimal point.
print(123 + 456)

# ----------------------------------------------------------------

# Floats: A float is a number that contains a decimal point and
# is used to represent real or fractional values.

print(12.5 - 10.2)

# ----------------------------------------------------------------

# Booleans: A boolean is a data type that represents one of two values: True or False.

print(True)
print(False)

# ----------------------------------------------------------------

# Type Conversion/Type Casting

num_in_str = "123"
print(num_in_str , type(num_in_str))

num_in_int = int(num_in_str) # Converting string to integer
print(num_in_int, type(num_in_int))

# ----------------------------------------------------------------

# Challenge 2 : Fix the len() function so it has no more warnings or errors.
# print(len(12345)) # TypeError

print(len("12345"))
print(len(str(12345)))

# ----------------------------------------------------------------

# Challenge 3: Write out 4 type checks to print all 4 data types

print(type("Hello"))
print(type(123))
print(type(12.44))
print(type(True))

# Challenge 4: Make this line of code run without errors:
# print("Number of letters in your name: " + len(input("Enter your name")))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# ----------------------------------------------------------------

# Mathematical Operators: + , - , * , / , // and **

print(2 + 2)  # Addition        # Output = 4
print(2 - 2)  # Subtraction     # Output = 0
print(2 * 2)  # Multiplication  # Output = 4
print(4 / 2)  # Division        # Output = 2.0
print(4 // 2) # Floor Division  # Output = 2
print(2 ** 2) # Exponent        # Output = 4

# ----------------------------------------------------------------

# Rule of calculation: PEMDAS (LEFT TO RIGHT)
# 1) Parentheses
# 2) Exponents
# 3) Multiplication/Division
# 4) Addition/Subtraction

# ----------------------------------------------------------------

# Challenge 5: What is the output of this code?
# print(3 * 3 + 3 / 3 - 3)

print(3 * 3 + 3 / 3 - 3) # Output = 7.0

# Breakdown of challenge 5:
# Step 1) 3 * 3    = 9    ,
# Step 2) 3 / 3    = 1.0  ,
# Step 3) 9 + 1.0  = 10.0 ,
# Step 4) 10.0 - 3 = 7.0

# ----------------------------------------------------------------

# Challenge 6: Change the code so it outputs 3?
# print(3 * 3 + 3 / 3 - 3)

print(3 * (3 + 3) / 3 - 3) # Output = 3.0

# Breakdown of challenge 6:
# Step 1) 3 + 3  = 6   ,
# Step 2) 3 * 6  = 18  ,
# Step 3) 18 / 3 = 6.0 ,
# Step 4) 6 - 3  = 3.0

# ----------------------------------------------------------------

# Challenge 7: BMI Calculator

height = 1.65
weight = 84

# Calculate the bmi using weight and height.
bmi = weight / (height * height)

print(bmi) # Output = 30.85399449035813

# ----------------------------------------------------------------

from math import floor

# Flooring a number:

print((int(bmi)))   # Output = 30
print((floor(bmi))) # Output = 30

# ----------------------------------------------------------------

# Rounding a number:

print(round(bmi)) # Output = 31
print(round(bmi,2)) # Output = 30.85

# ----------------------------------------------------------------

# Assignment Operators

num_01 = 22

num_01 += 2
print(num_01) # Output = 24

# Other Assignment Operators are:

# -= , *= , /= , **= , //=

# ----------------------------------------------------------------

# f-Strings = Format Strings

name = "Hamid"
age = 30
can_drive = True

print(f"My name is {name}. I am {age} years old. I can drive {can_drive}.")
