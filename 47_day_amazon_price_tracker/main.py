import requests
from bs4 import BeautifulSoup
import smtplib

product_link = 'https://www.amazon.com/dp/B08PQ2KWHS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
my_email = 'orustamxon@gmail.com'
password = 'qiwdjgqbjyelurjr'
test_price = 200.15
response = requests.get(url=product_link)
soup = BeautifulSoup(response.content, 'lxml')
price = soup.select('.celwidget .a-section .a-price span.a-offscreen')[1].getText()
price_without_currency = float(price.split("$")[1])
print(price_without_currency)

if price_without_currency < test_price:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='o7451155@yandex.com',
            msg=f'This product price is changed to {price_without_currency}\n{product_link}'
        )
