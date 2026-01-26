def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}" # Returns a value while calling the function.

print(format_name("HanzALA","HaMID")) # Returns an output

# ---------------------------------------------------

def function_1(text):
    return text + " " + text

def function_2(text):
    return text.title()

output = function_1("hello")
print(output)

# Using Function as an input for another function.
output_2 = function_2(output)
print(output_2)

output_3 = function_2(function_1("hello Hamid"))
print(output_3)

# ---------------------------------------------------

# Multiple Return Values:

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        # If this return gets executed the function will end here.!
        return "You didn't provide the valid information.!" 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("Enter your first name: "),input("Enter your second name: ")))

# ---------------------------------------------------

# Challenge : Leap Year
def is_leap_year(year):
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

print(is_leap_year(2000)) # True
print(is_leap_year(2024)) # True
print(is_leap_year(2021)) # False
print(is_leap_year(2026)) # False

# ---------------------------------------------------

# Documenting Functions

# A neat feature of docstrings is we can use it just below the definition of a function 
# and that text will be displayed when we hover over a function call. 
# It's a good way to remind ourself what a self-created function does.

def format_name(f_name, l_name):
    """Formats first name and last name together with title case.
    Takes two inputs: f_name , l_name
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)
print(length)

# ---------------------------------------------------

# We can also use docstrings to write multiline comments that document your code.


""" 
These 
type
of
multi - line
comments
are
not 
recommended
"""

