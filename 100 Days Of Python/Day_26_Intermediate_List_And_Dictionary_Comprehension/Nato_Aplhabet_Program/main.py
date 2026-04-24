import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# Turning DataFrame into Dictionary

data_dict = {row["letter"]:row["code"] for index,row in data.iterrows()}
# print(data_dict)

# Using nato_phonetic_alphabet.csv to Create a list of nato alphabets code

user_name = input("Enter Your Name: ")

phonetic_list = [data_dict[letter.upper()] for letter in user_name if letter.upper() in data_dict]

print(phonetic_list)