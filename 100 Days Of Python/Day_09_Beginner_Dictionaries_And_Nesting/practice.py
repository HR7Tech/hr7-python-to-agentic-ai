programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)

# ---------------------------------------------------

# Access item from the dictionary

print(programming_dictionary["Function"])

# ---------------------------------------------------

# Adding an item to the dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."

# ---------------------------------------------------

# Updating an existing item in the dictionary

programming_dictionary["Bug"] = "The moth in your computer."

# ---------------------------------------------------

# Using for loop with dictionary.

# Prints only keys

for item in programming_dictionary:
    print(item) 


# Prints both key and value

for key,value in programming_dictionary.items():
    print(key+":")
    print(value)

# Another way to print both key and value

for key in programming_dictionary:
    print(key+":")
    print(programming_dictionary[key])

# ---------------------------------------------------

# NESTED LISTS INSIDE DICTIONARY.

travel_log = {
    "France": ["Pairs", "Lille" ,["Lyon" , "Dijon"]],
    "Germany": ["Stuttgart", "Berlin"],
}

# Challenge 1: See if you can figure out how to print out 
# "Lille" from the nested List called travel_log.

# Solution:
print(travel_log["France"][1])

# ---------------------------------------------------

# NESTED LIST

nested_list = ["A","B",["C","D"]]

# Challenge 2: Try to print "D" from the list nested_list.

# Solution:
print(nested_list[2][1])

# ---------------------------------------------------

# NESTING DICTIONARY AND LISTS INSIDE A DICTIONARY

travel_log = {
    "France": {

        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,

    },

    "Germany":{

        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5,

    }
}

# Challenge 3: Figure out how to print out "Stuttgart" from the travel_log dictionary.

# Solution:
print(travel_log["Germany"]["cities_visited"][2])
