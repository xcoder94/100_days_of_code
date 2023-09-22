from tkinter import *
import requests
FONT = ('Arial', 30, 'bold')


def get_quote():
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()
    random_quote = response.json()['quote']
    print(random_quote)
    canvas.itemconfig(quote_text, text=random_quote)


# Window settings
window = Tk()
window.title('Kenya Says ...')
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file='./background.png')
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text='Kenya quote Goes Here', width=250,font=FONT, fill='white')
canvas.grid(row=0, column=0)

# Kenye button
kenye_img = PhotoImage(file='./kanye.png')
kenye_button = Button(image=kenye_img, highlightthickness=0, command=get_quote)
kenye_button.grid(row=1, column=0)






window.mainloop()

