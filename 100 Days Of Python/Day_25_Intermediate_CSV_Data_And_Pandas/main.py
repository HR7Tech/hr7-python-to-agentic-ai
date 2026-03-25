# with open("./Day_25_Intermediate_CSV_Data_And_Pandas/weather_data.csv") as data_file:
#     data = data_file.readlines()

# print(data)    

# ------------------------------------------

# import csv

# with open("./Day_25_Intermediate_CSV_Data_And_Pandas/weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
        
#     print(temperatures)    

# ------------------------------------------

import pandas as pd

data = pd.read_csv("./Day_25_Intermediate_CSV_Data_And_Pandas/weather_data.csv")

# print(type(data)) # DataFrame Object
# print(data)

# print(type(data["temp"])) # Series Object
# print(data["temp"])

# Converting data to python ditionary (DataFrame Object)
# data_dict = data.to_dict()
# print(data_dict)

# Converting a series into python list (Series Object)

# temp_list = data["temp"].to_list()
# print(temp_list)

# Perfomring different maths functions on temprature

# print(data["temp"].mean())
# print(data["temp"].max())

# Get columns from data (Both methods are correct)

# print(data["day"]) 

# or

# print(data.day)


# Get rows from the data

# print(data[data.day == "Monday"])

# The row with highest temp
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# print(monday.temp)

# monday.temp = 53.6 # Value Updated.

# print(monday.temp)

# Create DataFrame from the scratch

student_dict = {
    "names" : ["Hamid","Hanzala","Hamnu"],
    "marks" : [80,100,90]
}

data = pd.DataFrame(student_dict)
data.to_csv("./Day_25_Intermediate_CSV_Data_And_Pandas/new_data.csv")
print(data)

