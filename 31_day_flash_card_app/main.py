from tkinter import *
import pandas as pd
import random


# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_FOR_LANG = ('Ariel', 40, 'italic')
FONT_FOR_WORD = ('Ariel', 60, 'bold')

# pandas DataFrame
to_learn = {}
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

# -------------------- Funtions ---------------------------------------------- # 
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_image, image=front_card_image)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():    
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_image, image=back_card_image)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

#Creating a new window and configurations
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# UI Images
front_card_image = PhotoImage(file='images/card_front.png')
back_card_image = PhotoImage(file='images/card_back.png')
cross_image = PhotoImage(file='images/wrong.png')
check_image = PhotoImage(file='images/right.png')

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='', font=FONT_FOR_LANG)
card_word = canvas.create_text(400, 253, text='', font=FONT_FOR_WORD)


# Buttons
wrong_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)
right_btn = Button(image=check_image, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)




next_card()
# 

window.mainloop()