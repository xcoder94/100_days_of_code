from tkinter import *
import time

# Window settings
root = Tk()
root.title('Watermark GUI layout')
root.geometry('900x600')
root.config(padx=5, pady=5, bg='skyblue')
root.resizable(True, True)

# Create text widget and specify size.
text = Text(root, height=5, width=52)

# Create label
label = Label(root, text='Fact of the Day')
label.config(font=('Courier', 14))

random_words = 'apple banana carrot dinosaur elephant fantasy galaxy harmony iceberg journey kingdom lantern mountain notebook ocean pyramid quantum rainbow sunshine tornado umbrella volcano whisper xylophone yellow zebra adventure bicycle chocolate dragonfly'

# Split random_words into a list of words
words_list = random_words.split()

text.insert(END, random_words)
text.config(state=DISABLED)  # Make the text widget read-only

# Input for typing in GUI
input_for_type = Entry(root, width=30, state=DISABLED)

# Start button
start_btn = Button(root, text='Start')

# Points and mistakes labels
points_label = Label(root, text='Points: 0', font=('Courier', 14))
mistakes_label = Label(root, text='Mistakes: 0', font=('Courier', 14))

# Timer label
timer_label = Label(root, text='Time left: 60', font=('Courier', 14))

# GUI Layout
label.grid(row=0, column=0)
text.grid(row=1, column=0)
start_btn.grid(row=1, column=1)
timer_label.grid(row=1, column=2)
input_for_type.grid(row=2, column=0)
points_label.grid(row=3, column=0)
mistakes_label.grid(row=3, column=1)

current_word_index = 0  # Initialize word index tracker
points = 0  # Initialize points
mistakes = 0  # Initialize mistakes
time_left = 60  # Timer starts from 60 seconds


def check_word(event):
    global current_word_index, points, mistakes
    if event.keysym == 'space':  # Check if the Space key is pressed
        typed_word = input_for_type.get().strip()
        if typed_word == words_list[current_word_index]:
            points += 1
            points_label.config(text=f'Points: {points}')
            print(f"Correct! Points: {points}")
        else:
            mistakes += 1
            mistakes_label.config(text=f'Mistakes: {mistakes}')
            print(f"Incorrect! Mistakes: {mistakes}")
        current_word_index += 1
        if current_word_index >= len(words_list):
            print(f'End of text reached. Total Points: {points}, Total Mistakes: {mistakes}')
            input_for_type.unbind('<space>')
        input_for_type.delete(0, END)  # Clear the input field for the next word


def start_typing():
    input_for_type.config(state=NORMAL)
    input_for_type.focus_set()
    start_btn.config(state=DISABLED)
    countdown(time_left)


def countdown(count):
    global time_left
    timer_label.config(text=f'Time left: {count}')
    if count > 0:
        root.after(1000, countdown, count - 1)
    else:
        input_for_type.config(state=DISABLED)
        input_for_type.unbind('<space>')


# Bind the Space key press event to the Entry widget
input_for_type.bind('<space>', check_word)
start_btn.config(command=start_typing)

root.mainloop()
