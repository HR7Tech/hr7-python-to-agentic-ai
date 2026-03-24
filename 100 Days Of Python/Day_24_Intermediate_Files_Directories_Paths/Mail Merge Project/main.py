#TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
with open("./Day_24_Intermediate_Files_Directories_Paths/Mail Merge Project/Input/Letters/starting_letter.txt") as f:
    letter = f.read()

# print(letter)

with open("./Day_24_Intermediate_Files_Directories_Paths/Mail Merge Project/Input/Names/invited_names.txt") as f:
    name_list = f.readlines()

# print(name_list)

for name in name_list:
    striped_name = name.strip("\n")
    final_letter = letter.replace("[name]",striped_name)
    with open(f"./Day_24_Intermediate_Files_Directories_Paths/Mail Merge Project/Output/ReadyToSend/Letter for {striped_name}.txt","w") as f:
        f.write(final_letter)