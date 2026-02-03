# Debugging Odd or Even

# Before Debugging:

# def odd_or_even(number):
#     if number % 2 = 0: # Error
#         return "This is an even number."
#     else:
#         return "This is an odd number."

# Afer Debugging:

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

# ---------------------------------------------------

# Debugging Leap Year

# Before Debugging:

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0: # Error
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False    

# After Debugging:

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
# ---------------------------------------------------

# Debugging FizzBuzz

# Before Debugging:

# Target is the number up to which we count
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0: # Error 1
#             print("FizzBuzz")
#         if number % 3 == 0: # Error 2
#             print("Fizz")
#         if number % 5 == 0: # Error 3
#             print("Buzz")
#         else:
#             print([number]) # Error 4

# After Debugging:

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

