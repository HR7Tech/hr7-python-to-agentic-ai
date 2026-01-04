# Project: Bill Roulette (Who will pay the bill $$$)

# Objective: Pick a random name from the list of friends.

import random

# random.choice picks a random value from the list.!

# Option 1:

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_number = random.randint(0,len(friends) - 1)

print(f"Bill will be paid by: {friends[random_number]}.")

# -------------------------------------------------

# Option 2:

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_person = random.choice(friends)

print(f"Bill will be paid by: {random_person}.")

# -------------------------------------------------

# Option 3:

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(f"Bill will be paid by: {random.choice(friends)}")