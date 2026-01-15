import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# EASY VERSION: LETTERS => SYMBOLS => NUMBERS

password = ""

# Loop for letters.
for _ in range(nr_letters):
    password += random.choice(letters)

# Loop for symbols.
for _ in range(nr_symbols):
    password += random.choice(symbols)

# Loop for numbers.
for _ in range(nr_numbers):
    password += random.choice(numbers)

print(password)

# -------------------------------------------------

# HARD VERSION: RANDOM SELECTION BETWEEN LETTERS , SYMBOLS & NUMBERS

password = []

# Loop for letters.
for _ in range(nr_letters):
    password.append(random.choice(letters))

# Loop for symbols.
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

# Loop for numbers.
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

# print(password)

# The random.shuffle() function randomly rearranges the elements of a list in place.
random.shuffle(password)

final_password = ""

for char in password:
    final_password += char

print(final_password)