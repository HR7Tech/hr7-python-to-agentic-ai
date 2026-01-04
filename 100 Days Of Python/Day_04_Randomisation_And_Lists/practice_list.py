fruits = ["Grapes","Banana","Oranges","Kiwi","Apples"]
print(fruits)
print(type(fruits))

# -------------------------------------------------

# Indexing starts from 0. Negative indexing calls the item from the end.
print(fruits[0]) # Grapes
print(fruits[-1]) # Apples

# -------------------------------------------------

# Updating an item from the list.
fruits[0] = "Oranges"
print(fruits)

# -------------------------------------------------

# Adding a single item at the end of the list.
fruits.append("Pomegranate")
print(fruits)

# -------------------------------------------------

# Adding multiple items inside the list.
fruits.extend(["Strawberry","Watermelon"])
print(fruits)

# -------------------------------------------------

# Insert an item at a given position.
fruits.insert(0,"Coconut")
print(fruits)

# -------------------------------------------------

# Removes the first occurrences item from the list whose values is equal to x.
# Returns error if value not found in the list.!
fruits.remove("Apples")
print(fruits)

# -------------------------------------------------

# Removes the last item from the list.
fruits.pop()
print(fruits)

# -------------------------------------------------

# Counts the number of times value in list.
print(fruits.count("Oranges"))

# -------------------------------------------------

# Sorts the values in the list in ascending order.
fruits.sort()
print(fruits)

# -------------------------------------------------

# Reverse the elements of the list.
fruits.reverse()
print(fruits)

# -------------------------------------------------

# Returns a shallow copy of a list.

fruits2 = fruits.copy()
print(fruits2)

# Clears all the items from the list.
fruits2.clear()
print(fruits2)

print(fruits) # Original list remains same.!

