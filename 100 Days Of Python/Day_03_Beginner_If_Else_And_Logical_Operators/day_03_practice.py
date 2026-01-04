# Comparator Operators:

# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

# ---------------------------------------------------

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.!")
else:
    print("You cannot ride the rollercoaster.!")

# ---------------------------------------------------

# Challenge 1: BMI Calculator:

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")

# ---------------------------------------------------

# Challenge 2: ODD OR EVEN

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# ---------------------------------------------------

# Nested If/Else:

maths_score = 100
english_score = 95

if maths_score > 90:
    if english_score > 90:
        print("You are good at everything.!")
    else:
        print("Your are good at maths only.!")
else:
    print("You need to work harder..!!")

# ---------------------------------------------------

# Multiple If's:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child Ticket: $5.")
        bill += 5
    elif age <= 18:
        print("Teens Ticket: $7.")
        bill += 7
    else:
        print("Elders Ticket: $12.")
        bill += 12

    photo = input("Do you want to take a picture? Y or N: ($3 Charges) ").lower()
    if photo == "y":
        bill += 3

    print(f"Please pay ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

# ---------------------------------------------------

# Logical Operators:

a = 2 
b = 3

# 1) AND 

# True  + True  = True
print(a < b and a != b) # Output = True

# True  + False = False
print(a < b and a == b) # Output = False

# False + True  = False
print(a > b and a != b) # Output = False

# False + False = False
print(a > b and a == b) # Output = False


# 2) OR

# True  + True  = True
print(a < b or a != b) # Output = True

# True  + False = True
print(a < b or a == b) # Output = True

# False + True  = True
print(a > b or a != b) # Output = True

# False + False = False
print(a > b or a == b) # Output = False


# 3) NOT

# What's True will be False. What's False will become True.

print(not a > b and a != b) # Output = True

print(not a < b and  a != b) # Output = False

print(a > b or not a == b) # Output = True

print(a == b or not a != b) # Output = False