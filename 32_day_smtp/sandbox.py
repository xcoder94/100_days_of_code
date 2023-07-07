import smtplib
import datetime as dt
import random

my_email = 'orustamxon@gmail.com'
password = 'qiwdjgqbjyelurjr'

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs='o7451155@yandex.com', msg='Subject:Hello\n\nThis is The body of my mail')


now = dt.datetime.now()
year = now.year
month = now.month
num_of_day_in_week = now.weekday()
name_of_day_in_week = now.strftime('%A')
# print(name_of_day_in_week)

date_of_birth = dt.datetime(year=1994, month=1, day=24)
# print(date_of_birth)

if num_of_day_in_week == 4:
    with open('quotes.txt') as quotes:
        quotes = quotes.read()
        quotes_list = quotes.split('\n')
        random_quote = random.choice(quotes_list)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='o7451155@yandex.com', msg=f'Subject:Hello it\'s {name_of_day_in_week}\n\n{random_quote}')
else:
    print('other day')