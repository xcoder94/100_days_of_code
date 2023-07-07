from datetime import datetime
import pandas as pd
import random
import smtplib

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv('./birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f'./letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])

    my_email = 'orustamxon@gmail.com'
    password = 'qiwdjgqbjyelurjr'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_person['email'], 
            msg=f"Subject:Happy birthday!\n\n{contents}")






