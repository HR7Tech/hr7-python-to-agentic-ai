from tkinter import *

window = Tk()
window.minsize(200,100)
window.title("MILES TO KM PROJECT")

def calculate():
    mile_to_km = round(int(user_input.get()) * 1.609,2)
    answer_label.config(text =f"{mile_to_km}" )

user_input = Entry(width=10)
user_input.grid(row=0,column=1)

miles_label = Label(text="Miles",font=["Ariel",10,"italic"])
miles_label.grid(row=0,column=2)

is_equal_label = Label(text="Is Equal To",font=["Ariel",10,"italic"])
is_equal_label.grid(row=1,column=0)

answer_label = Label(text="00",font=["Ariel",10,"italic"])
answer_label.grid(row=1, column=1)

km_label = Label(text="KM",font=["Ariel",10,"italic"])
km_label.grid(row=1,column=2)

button = Button(text="Calculate Now",command= calculate)
button.grid(row=2,column=1)


window.mainloop()