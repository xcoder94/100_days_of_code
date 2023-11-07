import requests
import json
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_params = {
    'apikey': '0V57TLHYDQ90CL9N',
    'function': 'TIME_SERIES_DAILY',
    # 'function': 'TIME_SERIES_INTRADAY',
    # 'interval': '60min',
    'symbol': STOCK_NAME,
    # 'outputsize': 'full'
}

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
#    [new_value for (key, value) in dictionary.items()]
api_response = requests.get(STOCK_ENDPOINT, params=api_params)
api_response.raise_for_status()
stock_data = api_response.json()['Time Series (Daily)']
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)
# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)
# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#    Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100, 2)
# If TODO4 percentage is greater than 5 then print("Get News").

#   STEP 2: https://newsapi.org/
#   Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 5:
    news_api_params = {
        'q': COMPANY_NAME,
        'language': 'en',
        'apiKey': '00b8a0555bf5495f9a49a5146fd766ec'
    }
    news_response = requests.get(NEWS_ENDPOINT, news_api_params)
    articles = news_response.json()['articles']
# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f'Headline: {articles["title"]}. \nBrief: {articles["description"]}' for articles in three_articles]
#   TODO 9. - Send each article as a separate message via Twilio.
client = Client(account_sid, auth_token)
for article in formatted_articles:
    message = client.messages.create(
            body=article,
            from_='+15017122661',
            to='+998998205414'
        )

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
