print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip_calculate = bill * (tip / 100)
total_bill = tip_calculate + bill
per_head = total_bill / people

print(f"Total Bill: ${total_bill:.2f}") # :.2f means = Only 2 values after decimal point.!
print(f"Each Person Would Pay: ${per_head:.2f}")  

# ANTOHER WAY TO CODE THIS PROJECT:

total_bill_with_tip = bill + (bill * (tip / 100))
bill_per_person = total_bill_with_tip / people

print(f"Total Bill: ${total_bill_with_tip:.2f}")
print(f"Each Person Would Pay: ${bill_per_person:.2f}")