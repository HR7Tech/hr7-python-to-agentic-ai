# try = error => except executed
try:
    a_dict = {"name":"hamid","age":30}
    print(a_dict["ag"])
except KeyError:
    print("There is an error inside 'try' block.")
else:
    print("There is no error inside 'try' block.")

# try = no error => else executed
try:
    file = open("file.txt","w")
except FileNotFoundError:
    print("File Not Found ?")
else:
    print("File Found")
    file.close()

# try = error => except executed
try:
    file = open("file.txt","w")
    a_list = [1,2,3]
    print(a_list[3])
except IndexError:
    print("There is an error inside 'try' block.")
else:
    print("There is no error inside 'try' block")

# try = error => except executes => finally executes
try:
    open("a_new_file.txt","r")
except FileNotFoundError:
    print("a_new_file doesn't exist")
else:
    print("a_new_file exists")
finally:
    print("FINALLY WILL RUN , IT DOESN'T CARE IF a_new_file EXIST OR NOT")


# raising our own exceptions

players = int(input("How many players you have in your team: "))

if players > 11:
    raise ValueError("No teams are allowed to have more than 11 players.!")
else:
    print(players)

# --------------------------------------------------------

import json

a_dict = {"person":
         {"name":"Hamid","age":30},
          "person2":
              {"name":"Hanzala","age":"6 months"}
          }

# json.dump — Writes Python data into a JSON file:
with open("file.json","w") as file:
    json.dump(a_dict,file,indent = 3) # Saving Updated Data

# json.load — Reads JSON data from a file back into Python:
with open("file.json","r") as file:
    data = json.load(file) # Loads the already written data

    # .update() — This is actually a Python dictionary method, not a JSON method.
    # It merges one dictionary into another:

    data.update(a_dict) # Updated it with new data

with open("file.json","w") as file:
    json.dump(a_dict,file,indent = 3) # Saving Updated Data
    