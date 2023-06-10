from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    # Reset timer_text to 00:00
    canvas.itemconfig(timer_text, text='00:00')
    # Reset title_label to 'Timer'
    title_label.config(text='Timer', fg=GREEN)
    # Reset check_marks to ''
    check_status_label.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ----------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    # If it's the 8 rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)

    # If it's the 2nd/4th/6th rep
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------ # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'
    canvas.itemconfig(timer_text, text=f'{count_minutes}:{count_seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✓'
        check_status_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)



title_label = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

# Timer start button 
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

# status info 
check_status_label = Label(font=('Arial', 24, 'bold'), fg=GREEN, bg=YELLOW)
check_status_label.grid(row=3, column=1)

# Timer reset button 
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)



window.mainloop()
