from tkinter import *

# tkinter.TK() Creates a window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

def button_clicked():
    print("Congratulation For Getting Discount.!")
    new_text = user_input.get()
    my_label.config(text = new_text)

# There are three ways to display the widget.
# .pack()
# .place(x=..,y=..)
# .grid(row = ..,column = ..)
# .pack() and .row() cannot be used inside one single program

# A tkinter.Label() is just a widget used to display text or an image on the window.
my_label = Label(text="My First Label",font=["Ariel",20,"italic"])
my_label.config(text = "To Avail Discount.!",font=("Aries",10,"bold")) # my_label updated

# my_label.pack() # Default side = "up". | [up,bottom,left,right]
# my_label.place(x=100,y=200)
my_label.grid(row=0,column=0)

# tkinter.Button() Creates A BUTTON.!
button = Button(text="Subscribe Now",command=button_clicked)
button.grid(row=1,column=1)
new_button = Button(text="New Button",command=button_clicked)
new_button.grid(row=0,column=2)

# A tkinter.Entry() is just a widget used to display placeholder on the window.
user_input = Entry(width=10)
# user_input.insert(END,string="Write Something Here.") # prompt for the user
user_input.grid(row=2,column=3)


window.mainloop() # Keeps the window open until user closes it.

