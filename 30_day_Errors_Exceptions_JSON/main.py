from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------ #

def geenerate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letter_for_password = [random.choice(letters) for _ in range(nr_letters)]
    numbers_for_password = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_for_password = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = letter_for_password + numbers_for_password + symbols_for_password

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD  ---------------------- #
def save_pass():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if website == '' or email == '' or password == '':
        warning = messagebox.showwarning(title='OOPS', message='Please don\'t leave any fields empty!')
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updateing old data with new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


def find_password():
    entered_website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        warning = messagebox.showwarning(title='OOPS', message='No data file found')
    else:
        if entered_website in data:
            email = data[entered_website]['email']
            password = data[entered_website]['password']
            show_log_pass = messagebox.showinfo(title=f'{entered_website}', message=f'Email: {email}\npassword: {password}')
        else:
            no_data_showwarning = messagebox.showinfo(title=f'{entered_website}', message='No details for the website exist')


# ---------------------------- UI SETUP ------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')
# window.minsize(width=400, height=220)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image) # first 100 is position in x axis
canvas.grid(row=0, column=1)

# User form 
# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Inputs
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'test1@test.ru')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_btn = Button(text='Search', width=13, command=find_password, highlightthickness=0)
search_btn.grid(row=1, column=2)
generate_btn = Button(text='Generate password', command=geenerate_pass, highlightthickness=0)
generate_btn.grid(row=3, column=2)
add_button = Button(text='Add', command=save_pass, width=36, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()

