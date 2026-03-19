# file = open("my_text.txt") # opens a file 

# content = file.read() # reads its entire contents as a string

# print(content)

# # We close a file to free system resources and ensure all data is properly saved and not corrupted.
# file.close() # closes a file

# ------------------------------------------------

# When we open a file using the 'with' keyword, 
# it is automatically closed after the block of code is executed.

# with open("my_text.txt",mode="r") as file: # mode = "r" means 'read' (Which is also a default behaviour)
#     content = file.read()
#     print(content)

# ------------------------------------------------

# In write "w" mode, we can write data to a file, but it overwrites and removes all existing content.

# with open("my_text.txt",mode="w") as file:
#     file.write("This is a new line")

# ------------------------------------------------

# In append mode ("a"), we can write data to a file, 
# and it adds the new content without removing the existing content.

with open("my_text.txt",mode="a") as file:
    file.write("\nThis is a new second line")

# ------------------------------------------------

# When we open a file in write mode ("w"), if a file with that name does not exist, 
# it is automatically created.

with open("new_file.txt","w") as file:
    file.write("Hello World.!")
    