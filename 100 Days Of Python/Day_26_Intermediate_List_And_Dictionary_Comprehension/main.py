# Challenge : Create a new list and add 1 to each item from the list "numbers"

# Old Fashion

# numbers = [1,2,3]
# print(numbers)
# new_list = []
# for num in numbers:
#     new_num = num + 1
#     new_list.append(new_num)
# print(new_list)

# List Comprehension
# [new_item for item in list if test] ==>> Formula


numbers = [1,2,3]
print(numbers)
new_list = [n + 1 for n in numbers]
print(new_list)

# List Comprehension With Strings

name = "Hamid"
new_name_list = [letter for letter in name]
print(new_name_list)

# List Comprehension With Range

range_list = [num * 2 for num in range(1,5)]
print(range_list)

# List Comprehension With Tests

friend_names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

short_name_friend = [name for name in friend_names if len(name) < 5]
print(short_name_friend)

long_name_uppercase = [name.upper() for name in friend_names if len(name) > 5]
print(long_name_uppercase)

# Some Practices

# Squared Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# Even Numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings] # Converting to integers
result = [num for num in numbers if num % 2 == 0]
print(result)

# Dictionary Comprehensions

import random
student_names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

student_scores = {student:random.randint(0,100) for student in student_names}

print(student_scores)

passed_students = {key:value for key,value in student_scores.items() if value >= 50}

print(f"Passed Students: {passed_students}")

failed_students = {student:score for student,score in student_scores.items() if score < 50}
print(f"Failed Students: {failed_students}")

# Some Practices:

# Word and It's Length as Key,Value Pair.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split()
result = {word:len(word) for word in word_list}
print(result)

# Celsius To Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:((temp * 9/5) + 32) for day,temp in weather_c.items()}
print(weather_f)

# Dict to DataFrame , Then Looping on DataFrame

import pandas as pd

student_data = {
    "student": ["Hamid","Ahmed","Raza"],
    "scores":[80,100,90]
}
student_Data_Frame = pd.DataFrame(student_data)
print(student_Data_Frame)

# For Loop on DataFrame.
# for key,value in student_Data_Frame.items():
#     print(key)
#     print(value)

# For Loop on Pandas DataFrame
for index , rows in student_Data_Frame.iterrows():
    # print(index)
    # print(rows)
    print(index,rows)

    # We Can Also Tap Into Attributes
    # print(rows.student)
    # print(rows.scores)
