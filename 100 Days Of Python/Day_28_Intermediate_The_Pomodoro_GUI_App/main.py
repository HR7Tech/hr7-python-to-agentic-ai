from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
# https://colorhunt.co/ FOR FONT COLORS

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#F7DD7D"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def restart():
    window.after_cancel(timer)
    timer_label.config(text="TIMER")
    canvas.itemconfig(time_text,text= "00:00")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60 # 1 , 3 , 5 , 7
    short_break_sec = SHORT_BREAK_MIN * 60 # 2 , 4 , 6
    long_break_sec = LONG_BREAK_MIN * 60 # 8

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="lONG BREAK",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text,text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        print(work_session)
        for _ in range(work_session):
            marks += "✔"
        tick_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100,pady=50,bg=YELLOW)
window.title("Pomodoro App")

timer_label = Label(text="TIMER",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)

canvas = Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image = image) # xcor = 102 , ycor = 112
time_text = canvas.create_text(105,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1 ,column=1)

start_button = Button(text="Start",font=(FONT_NAME,10,"bold"),bg=YELLOW,command=start_timer)
start_button.grid(row=2,column=0)

restart_button = Button(text="Restart",font=(FONT_NAME,10,"bold"),bg=YELLOW,command=restart)
restart_button.grid(row=2,column=2)

tick_label = Label(font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
tick_label.grid(row=3,column=1)

window.mainloop()

