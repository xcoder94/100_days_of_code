import requests
import json
from infobip_channels.sms.channel import SMSChannel

BASE_URL = "https://8gvkde.api.infobip.com"
API_KEY = "856ebe5e3d8b684f69594fe1f4e898cc-ae1a83fb-2c0a-4d63-8c87-482e96f6c3cf"
RECIPIENT = "998998205414"


def send_sms(message):
    # Initialize the SMS channel with your credentials.
    channel = SMSChannel.from_auth_params(
        {
            "base_url": BASE_URL,
            "api_key": API_KEY,
        }
    )

    # Send a message with the desired fields.
    sms_response = channel.send_sms_message(
        {
            "messages": [
                {
                    "destinations": [{"to": RECIPIENT}],
                    "text": f"{message}",
                }
            ]
        }
    )

    # Get delivery reports for the message. It may take a few seconds show the just-sent message.
    query_parameters = {"limit": 10}
    delivery_reports = channel.get_outbound_sms_delivery_reports(query_parameters)

    # See the delivery reports.
    print(delivery_reports)


STOCK_NAME = "TSLA"
COMPANY_NAME = "tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_params = {
    'apikey': '0V57TLHYDQ90CL9N',
    'function': 'TIME_SERIES_DAILY',
    # 'function': 'TIME_SERIES_INTRADAY',
    # 'interval': '60min',
    'symbol': STOCK_NAME,
    # 'outputsize': 'full'
}
news_api_params = {
    'q': COMPANY_NAME,
    'language': 'en',
    'apiKey': '00b8a0555bf5495f9a49a5146fd766ec'
}
# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#   TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
#    [new_value for (key, value) in dictionary.items()]
# stock_api_response = requests.get(STOCK_ENDPOINT, params=stock_api_params)
# stock_api_response.raise_for_status()
# stock_data = stock_api_response.json()['Time Series (Daily)']

# '''Her I create json file with stock prices, Because I have daily limit.'''
# with open('stock_prices.json', 'w') as data_file:
#     json.dump(stock_data, data_file, indent=4)

# '''And here I will open it for using'''
with open('stock_prices.json', 'r') as stock_data_file:
    stock_prices = json.load(stock_data_file)

last_10_days_stock_price = [value for (key, value) in stock_prices.items()]
yesterday_price = last_10_days_stock_price[1]['4. close']

#   TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_price = last_10_days_stock_price[2]['4. close']

#   TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#    Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = round(float(yesterday_price) - float(day_before_yesterday_price), 2)

#   TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# discrepancies in percentage - Расхождение в процентах
# Here we've founded how many percent increased the yesterday's price from day before yesterday's price
discrepancies = round(difference / float(day_before_yesterday_price) * 100, 2)

#   TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if discrepancies > 5:
#     print('+ get news')
# elif discrepancies < -5:
#     print('- get news')
#   STEP 2: https://newsapi.org/
#   Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#   TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_response = requests.get(NEWS_ENDPOINT, params=news_api_params)
news_response.raise_for_status()
news_data = news_response.json()
#   TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
#    Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
last_3_articles = [articles for articles in news_data['articles'][:3]]


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

#   TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
last_3_news = [{'title': article['title'], 'description': article['description']} for article in last_3_articles]
#   TODO 9. - Send each article as a separate message via Twilio.
for i in last_3_news:
    if discrepancies > 5:
        message = f'{STOCK_NAME} 🔺 {discrepancies} %\nHeadline: {i["title"]}\nBrief: {i["description"]}'
        send_sms(message)
    elif discrepancies < -5:
        message = f'{STOCK_NAME} 🔻 {discrepancies} %\nHeadline: {i["title"]}\nBrief: {i["description"]}'
        send_sms(message)
#   Optional TODO: Format the message like this:
""" 
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
