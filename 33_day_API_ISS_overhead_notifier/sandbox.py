import requests
from datetime import datetime
MY_LAT = 41.299496
MY_LONG = 69.240074
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_poition = (longitude, latitude)
# print(iss_poition)

# API Parameters
parameters = {
    'lat': MY_LAT,
    'long': MY_LONG,
    'formatted': 0
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

time_now = datetime.now()

print(sunrise)
print(sunset)



