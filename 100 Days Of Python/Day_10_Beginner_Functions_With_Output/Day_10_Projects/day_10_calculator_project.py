logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

        # -------------------------------------------------

# TODO-1: Creating 4 functions : add , subtract , multiply , divide

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# -------------------------------------------------

# TODO-2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
# Adding all 4 functions with keys as symbols inside dictionary.!

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# -------------------------------------------------

# TODO-3: Use the dictionary operations to perform the calculations.

# Creating a function called "calculator"

def calculator():
    continue_calculation = True # Will be used for while loop
    num1 = float(input("Enter first number: "))

    while continue_calculation:
        # Giving options to user to select an operation.
        for symbol in operations: 
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        # If the operation is not in the dictionary the calculation will be restarted.!
        if operation_symbol not in operations: 
            continue_calculation = False
            print("You type an invalid input.! Calculation will restart.!")
            calculator() # Using recursion to restart the function from the top.!
        
        # Else calculation goes on.!
        else: 
            num2 = float(input("Enter another number: "))

            # Saving the first/every calculation inside the variable 'answer'
            answer = operations[operation_symbol](num1,num2) 

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            # Giving user 3 choices:
            choice = input(f"Type 'y' to continue with {answer}.Type 'n' to start a new calculation.Type 'e' to exit: ").lower()

            # If Elif Else chain according to user input.!

            # If user wants to continue calculation the first input (num1) will be variable 'answer' automatically.!
            if choice == "y":
                num1 = answer 

            # If user wants new calculation then 25 empty lines will be printed and new calculation will be started.
            elif choice == "n": 
                print("\n" * 25)
                continue_calculation = False
                calculator() # Using recursion to restart the function from the top.!

            elif choice == "e":
                print("Goodbye.!")
                continue_calculation = False

            # If user inputs an invalid input the calculation will be restarted
            else: 
                continue_calculation = False
                print("You type an invalid input.! Calculation will restart.!")
                calculator() # Using recursion to restart the function from the top.!

calculator()