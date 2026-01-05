# My Project : Personal Budget And Expense Splitter

# This project builds a Personal Budget & Expense Splitter using Day 2 concepts such as 
# primitive data types, type conversion, mathematical operations, number manipulation, and f-strings.

print("Welcome to Personal Budget And Expense Splitter Application")

monthly_income = float(input("Enter your monthly income: "))

rent_expense = float(input("Enter your rent expense: "))

food_expense = float(input("Enter your food expense: "))

transport_expense = float(input("Enter your transport expense: "))

other_expenses = float(input("Enter your other expenses: "))

total_expenses = rent_expense + food_expense + transport_expense + other_expenses

remaining_amount = monthly_income - total_expenses

expense_percentage = (total_expenses / monthly_income) * 100

print(f"""

Monthly Income = {monthly_income:.2f}
Total Expenses = {total_expenses:.2f}
Remaining Amount = {remaining_amount:.2f}
Expense Percentage = {expense_percentage:.2f}%

""")

print("Budget Calculation Completed Successfully.")