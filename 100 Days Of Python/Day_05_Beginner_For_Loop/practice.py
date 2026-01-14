fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit) # prints each iteration
    print(f"{fruit} Pie") # prints each iteration with "Pie"
    print(fruits) # prints original list

print("Loop Ended") # will be printed once when the loops end.!

# -------------------------------------------------

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# -------------------------------------------------

# The sum() function returns the total of all numeric values in an iterable, such as a list.
total_student_scores = sum(student_scores)
print(total_student_scores)

# -------------------------------------------------

# The min() function returns the smallest value from an iterable or from the given arguments.
lowest_marks = min(student_scores)
print(lowest_marks)

# -------------------------------------------------

# The max() function returns the largest value from an iterable or from the given arguments.
highest_marks = max(student_scores)
print(highest_marks)

# -------------------------------------------------

marks = [8,65,89,86,55,91,64,89]

# Challenge 1: Find the highest mark in the 'marks' list without using 'max' function.!

highest_marks = 0

for score in marks:
    if score > highest_marks:
        highest_marks = score

print(highest_marks)

# -------------------------------------------------

# Challenge 2: Find the minimum mark in 'marks' list without using the 'min' function.!

lowest_marks = 100

for score in marks:
    if lowest_marks > score:
        lowest_marks = score

print(lowest_marks)

# -------------------------------------------------

# Challenge 3: Calculate the total marks in the 'marks' list without using the 'sum' function.!

total_student_marks = 0
for score in student_scores:
    total_student_marks += score

print(total_student_marks)

# -------------------------------------------------

for i in range(6): # The two arguments: Starting Point (Default as Zero) , Finishing Point.
    print(i)

# -------------------------------------------------

for i in range(1,11): # The two arguments: Starting Point , Finishing Point.
    print(i)

print("Loop Ended.")

# -------------------------------------------------

for i in range(0,11,2): # The three argument: Starting Point , Finishing Point , Skip.
    print(i)

print("Loop Ended.")

# -------------------------------------------------

# Challenge 4: The Gauss Challenge
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

add_1_to_100 = 0

for i in range(1,101):
    add_1_to_100 += i

print(add_1_to_100)

