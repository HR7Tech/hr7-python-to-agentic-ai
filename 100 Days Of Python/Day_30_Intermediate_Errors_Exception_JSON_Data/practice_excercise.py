# Exercise # 01:

# Objective : If the user enters something that is out of range just
# print a default output of "Fruit pie".

# Catch the exception and make sure the code runs without crashing.

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")

make_pie(4)

# --------------------------------------------------

# Exercise # 02:
# We've got some buggy code, try running the code.
# Objective: Use what you've learnt about exception handling to prevent the program from crashing.

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass

    return total_likes


count_likes(facebook_posts)

# -------------------------------------------

# Exercise # 03:

# Catch a KeyError when a user enters a character that is not in the dictionary
# Provide feedback to the user when an illegal word was entered
# Continue prompting the user to enter another word until they enter a valid word

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data)

data_dict = {row["letter"]:row["code"] for index,row in data.iterrows()}
print(data_dict)

while True:
    try:
        user_input = input("Enter Your Name: ").upper()
        if not user_input.isalpha():
            raise KeyError
    except KeyError:
        print("Sorry, Only Letters Allowed")
    else:
        nato_phonetic_list = [data_dict[letter] for letter in user_input]
        print(nato_phonetic_list)
        break

