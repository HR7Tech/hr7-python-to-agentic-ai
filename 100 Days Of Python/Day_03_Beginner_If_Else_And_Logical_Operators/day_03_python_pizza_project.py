# MENU:
# Small Pizza = $15
# Medium Pizza = $20
# Large Pizza = $25

# Extras:
# Pepperoni on Small Pizza = $2
# Pepperoni on Medium/Large Pizza = $3
# Extra Chees on any Pizza = $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0

if size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2

elif size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3

elif size == "l":
    bill = 25
    if pepperoni == "y":
        bill += 3

else:
    print("Invalid Input.!")

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")