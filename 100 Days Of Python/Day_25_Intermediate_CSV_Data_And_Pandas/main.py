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

print(type(data)) # DataFrame Object
print(data)

print(type(data["temp"])) # Series Object
print(data["temp"])

