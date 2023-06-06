from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_func():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_func():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', font=('Arial', 24, 'bold'), fg=GREEN)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

# Timer start button 
start_button = Button(text="Start", command=start_func)
start_button.grid(row=2, column=0)

# status info 
check_status_label = Label(text='✓', font=('Arial', 24, 'bold'), fg=GREEN)
check_status_label.grid(row=3, column=1)

# Timer reset button 
reset_button = Button(text="Reset", command=reset_func)
reset_button.grid(row=2, column=2)



window.mainloop()
