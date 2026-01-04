# My Project: Movie Ticket Pricing & Eligibility System

# This project applies Day 03 Python concepts such as control flow using if/elif/else,
# nested and multiple conditional statements, logical operators, and the modulo operator
# to calculate movie ticket prices based on user eligibility and conditions.

print("Welcome to HR7 Theatre - Movie Ticket Pricing System\nJANUARY 2026")

age = int(input("Enter your age: ")) # Pricing will affect on the age.

base_price = 0
discount = 0
vip_price = 0
final_ticket_price = 0


if age <= 12:
    base_price = 10
    final_ticket_price += base_price
elif age < 20:
    base_price = 20
    final_ticket_price += base_price
    is_student = input("Are you a student: 'Yes' or 'No' ").lower() # Students will get discounted price
    if is_student == "yes":
        discount += 5
        final_ticket_price -= discount

elif age <= 40:
    base_price = 40
    final_ticket_price += base_price
    is_student = input("Are you a student: 'Yes' or 'No' ").lower() # Students will get discounted price
    if is_student == "yes":
        discount += 5
        final_ticket_price -= discount

elif age > 40:
    base_price = 30
    final_ticket_price += base_price            

else:
    print("Invalid Input.. System will restart.!")


day_of_month = int(input("Day of the month: 1 - 31: ")) # For even days there would be discount
  
if day_of_month % 2 == 0:
    final_ticket_price -= discount
    discount += discount
    

vip_box = input("Do you want to sit in VIP section: 'Yes' or 'No': ").lower()

if vip_box == "yes":
    final_ticket_price += 10
    vip_price += 10
elif vip_box == "no":
    final_ticket_price = final_ticket_price
else:
    print("Invalid Input.. System will restart.!")

if day_of_month <= 31 and day_of_month > 0:
    print(f"""
    Base Price: ${base_price}
    Disocunt: - ${discount}
    Vip Charges: + ${vip_price}

    Final Ticket Price : ${final_ticket_price}

    """)
else:
    print("\nInvalid Day Selected. Ticket Not Confirmed.! Try Again.!")    