print("Welcome to Multiplication Table Generator.!")

number = int(input("Which numbers table you want? "))
limit = int(input("The limit up to which it should be generated: "))

for num in range(1, limit + 1):
    print(f"{number} x {num} = {number * num}")