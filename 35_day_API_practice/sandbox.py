import requests
from twilio.rest import Client

# MY_LAT = 41.331603
MY_LAT = 41.162849
# MY_LONG = 69.269170
MY_LONG = 71.559242
account_sid = 'US560db6129ba191de53756399b3c2a285'
auth_token = 'TWILIO_AUTH_TOKEN'
weather_parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'exclude': 'current,minutely,daily',
    'appid': 'OWM_API_KEY'
    # 'appid': '55a991e2204c206a86e8bfe8dde2c2fb'
}
response = requests.get(
    # url='https://api.openweathermap.org/data/2.5/weather',
    url='https://api.openweathermap.org/data/3.0/onecall',
    params=weather_parameters
)
response.raise_for_status()
weather_data = response.json()

last_twelve_hours = []

for i in weather_data['hourly'][:12]:
    last_twelve_hours.append(i['weather'][0]['id'])


def notify_to_pick_umbrella(twelve_hours):
    rainy = None
    for hour_id in twelve_hours:
        if hour_id <= 700:
            rainy = True
            break
        else:
            rainy = False
    if rainy:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body='Bring an umbrella',
                from_='+15017122661',
                to='+998998205414'
            )
        print(message.status)
    else:
        print('Don\'t pick an umbrella')
    return rainy


notify_to_pick_umbrella(last_twelve_hours)
# print(weather_data)
# print(last_twelve_hours)
