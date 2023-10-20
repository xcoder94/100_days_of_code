import requests

MY_LAT = 41.331603
MY_LONG = 69.269170
weather_parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'exclude': 'hourly,daily',
    # 'appid': '55a991e2204c206a86e8bfe8dde2c2fb'
    'appid': '592cae270c49b7927456b7e3e08fd70b'
}
response = requests.get(
    # url='https://api.openweathermap.org/data/2.5/weather',
    url='https://api.openweathermap.org/data/3.0/onecall',
    params=weather_parameters
)
response.raise_for_status()
weather_data = response.json()
