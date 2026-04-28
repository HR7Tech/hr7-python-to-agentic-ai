from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for number in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_clicked():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if any field is empty
    if not website or not email or not password:
        messagebox.showwarning(title="Oops!", message="Please don't leave any field empty!")
        return

    # Confirm before saving
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:"
                f"\nEmail: {email}\nPassword: {password}\n\nIs it ok to save?"
    )

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager GUI App")

image = PhotoImage(file="logo.png")
canva = Canvas(width=200,height=200,)
canva.create_image(100,100,image=image)
canva.grid(row=0,column=1)

# Website Label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

# Email/Username Label
emai_label = Label(text="Email/Username:")
emai_label.grid(row=2,column=0)

# Password Label
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


# Website Entry
website_entry = Entry(width=60)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

# Email/Username Entry
email_entry = Entry(width=60)
email_entry.grid(row=2,column=1,columnspan=2)

# Password Entry
password_entry = Entry(width=40)
password_entry.grid(row=3,column=1)


# Generate Password Button
generate_password_button = Button(text="Generate Password",command=password_generator)
generate_password_button.grid(row=3,column=2)

# Add Button
add_button = Button(text="ADD",width=50,command=add_button_clicked)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()