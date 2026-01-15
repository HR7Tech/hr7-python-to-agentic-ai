import random

print("Welcom to Treasure Box.!")
print("Find the Treasure marked as 'X'.\n")

# CREATE a 3x3 map using nested lists filled with empty symbols:

map = [["⬜","⬜","⬜"],
       ["⬜","⬜","⬜"],
       ["⬜","⬜","⬜"]]


# GENERATE a random row number:
random_row = random.randint(0 , len(map) - 1) # Genrate a random integer between 0 - 2
# print("row = ", random_row + 1)


# GENERATE a random column number:
random_column = random.randint(0 , len(map) - 1) # Genrate a random integer between 0 - 2
# print("column = ",random_column + 1)


# DISPLAY the map without revealing the treasure:
print(map[0])
print(map[1])
print(map[2])


# ASK user to select a row number:
user_row = int(input("Select row number: 1 , 2 , 3: "))

# ADJUST row number for list index
user_row -= 1


# ASK user to select a column number:
user_column = int(input("Select column number: 1 , 2 , 3: "))

# ADJUST column number for list index
user_column -= 1


# HIDE treasure (X) at the random column and row position in the map:
map[random_row][random_column] = "X"


# CHECK does user found the treasure or not:
if random_row == user_row and random_column == user_column:
    print("Hurray...!! You found the treasure..!!")
else:
    print("\nWrong Guess...\nGame Over..!!\n")
    map[user_row][user_column] = "O"


# DISPLAY the final map:    
print(map[0])
print(map[1])    
print(map[2])     

