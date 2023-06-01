from tkinter import *

# Learning
# def button_clicked():
#     print('I got clicked')
#     new_text = input.get()
#     my_label.config(text=new_text)


# window = Tk()
# window.title('My first GUI program')
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)


# # Label
# my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
# my_label.config(text='New text')
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# # Button
# button = Button(text='click me', command=button_clicked)
# button.grid(column=1, row=1)
# new_button = Button(text='New button', command=button_clicked)
# new_button.grid(column=2, row=0)

# # Entry
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3, row=2)


# Day project. Mile to Km converter

window = Tk()
window.title('Mile to Km converter')
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)


def mile_to_km():
    entered_data = int(mile_input.get())
    converted_data = entered_data * 1.609
    converted_km.config(text=round(converted_data, 3))

# Mile input
mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)

# Labels
mile = Label(text='miles', font=('Arial', 16))
mile.grid(row=0, column=2)

is_equal_to = Label(text='is equal to', font=('Arial', 16))
is_equal_to.grid(row=1, column=0)

converted_km = Label(text='0', font=('Arial', 16))
converted_km.grid(row=1, column=1)
km_text = Label(text='Km', font=('Arial', 16))
km_text.grid(row=1, column=2)

# Calculate Button
calculate_btn = Button(text='Calculate', command=mile_to_km)
calculate_btn.grid(row=2, column=1)















window.mainloop()

