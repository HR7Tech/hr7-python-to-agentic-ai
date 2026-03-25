import pandas as pd


data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"]) # length of rows
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"]) # length of rows
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"]) # length of rows

# print(red_squirrels_count)
# print(black_squirrels_count)
# print(gray_squirrels_count)

color_dict = {
    "Fur Color" : ["red","black","gray"],
    "Count" : [red_squirrels_count,black_squirrels_count,gray_squirrels_count]
}

data = pd.DataFrame(color_dict)

data.to_csv("./squirrel_count.csv")