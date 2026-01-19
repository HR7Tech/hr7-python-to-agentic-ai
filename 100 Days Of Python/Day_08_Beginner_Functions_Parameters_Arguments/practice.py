# FUNCTION WITH PARAMETERS AND ARGUMENTS..

def greet_with_name(name): # name is parameter
    print(f"Hello {name}.")
    print(f"How are you {name}?")

greet_with_name("Hamid") # Hamid is an argument

# -------------------------------------------------

def greet(name):
    name = name.upper()
    print(f"Hello {name}")

greet("hamid")

# -------------------------------------------------

# FUNCTIONS WITH MULTIPLE PARAMETERS.

def greet_with(name,location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")


# Positional Arguments
greet_with("Hamid","Karachi")

# Keyword Arguments
greet_with(location="Karachi",name="Hamid")