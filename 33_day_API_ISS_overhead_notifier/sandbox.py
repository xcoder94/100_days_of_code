import requests
from datetime import *
# from tkinter import *

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)
# print(iss_position)


# def get_quote():
    # response = requests.get(url='https://api.kanye.rest')
    # response.raise_for_status()
    # random_quote = response.json()['quote']
    # print(random_quote)
    # canvas.itemconfig(quote_text, text=random_quote)



# Window create and configuration
# window = Tk()
# window.title('Kenye Says ...')
# window.config(padx=50, pady=50)

# # Canvas
# canvas = Canvas(width=300, height=414)
# bg_img = PhotoImage(file='background.png')
# canvas.create_image(150, 207, image=bg_img)
# quote_text = canvas.create_text(150, 207, text='Kanye quote Goes here', width=250, font=('Arial', 30, 'bold'))
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file='kanye.png')
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,)
# kanye_button.grid(row=1, column=0)


# window.mainloop()

# Constants
MY_LAT = 41.299496
MY_LNG = 69.240074

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    # 'date': 'DD-MM-YYYY',
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]


time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)












