# Modules in Python:

# Python allows us to put code into different files and import that code 
# if needed. This means that we can better organise and modularise our code.

import random # random is a python module.

# -------------------------------------------------

# random.randint(a,b) - Generates a random integer between given values a (inclusive) and b (inclusive) .

random_integer = random.randint(0,10)

print(random_integer)

# -------------------------------------------------

# random.random() - Generates a random floating point value between 0 (inclusive) and 1 (exclusive)

random_0_to_1 = random.random()
print(random_0_to_1)

random_0_to_n = random.random() * 10
print(random_0_to_n)

# -------------------------------------------------

# random.uniform(a,b) - Generates a random floating point number
# between given values a (inclusive) and b (inclusive).

random_floating = random.uniform(0,10)

print(random_floating)

# -------------------------------------------------

# Challenge: Heads or Tails
 
heads_or_tails = random.randint(0,1)

print(heads_or_tails)

if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
    