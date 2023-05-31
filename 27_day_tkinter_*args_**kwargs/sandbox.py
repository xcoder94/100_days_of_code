from tkinter import *

window = Tk()
window.title('My First Gui program')
window.minsize(width=500, height=300)

# Label
my_label = Label(text='I am a LAbel', font=('Arial', 24, 'bold'))
my_label.pack()

my_label['text'] = 'New text'
my_label.config(text='New text')

# inputs
gui_input = Entry(width=30)
gui_input.pack()

# Buttons

def button_click():
    my_label.config(text=gui_input.get())


button = Button(text='Click me', command=button_click)
button.pack()

window.mainloop()

# def add(*args):
#     summ_args = 0
#     for i in args:
#         summ_args += i
#     return summ_args

# print(add(1,2,3))

# def calculate(n, **kwargs):
    # print(kwargs) # type of **kwargs is dict
    # for k, v in kwargs.items():
    #     print(k)
    #     print(v)
    # n += kwargs['add']
    # n *= kwargs['multiply']
    # print(n)


# calculate(2, add=3, multiply=5)


# class Car:

#     def __init__(self, **kw):
#         self.make = kw.get('make')
#         self.model = kw.get('model')
#         self.color = kw.get('color')
#         self.seats = kw.get('seats')


# my_car = Car(make='Nissan', model='GTR')
# print(my_car.model)