user_email = "admin"
user_password = "admin"

def login_successful():
    print("\nYou are logged in.!")

def change_email():
    new_email = input("Enter your new email: ")
    return new_email

def change_password():
    new_password = input("Enter your new password: ")
    return new_password

is_active = True

while is_active:
    user_id = input("Enter your email: ")
    user_pass = input("Enter your password: ")

    if user_id == user_email and user_pass == user_password:
        login_successful()
        user_choice = input("""Do you want to change your email ID: Type 'I'
Do you want to change your password: Type 'P'       
Press 'e' to exit:                    
""").lower()    
    
        if user_choice == "e":
            is_active = False
            print("\nGood Bye.!")

        elif user_choice == "i":
            user_email = change_email()
            print("\nEmail Change.!")
            print("Please login again with your new email.! Thank You\n")
        
        elif user_choice == "p":
            user_password = change_password()
            print("\nPassword Change.!")
            print("Please login again with your new password.! Thank You\n")

        else:
            print("\nYou are logged out.!") 
            print("Sign In again.\n")   

    else:
        print("\nWrong Email or Password.! Try Again.!\n")        



