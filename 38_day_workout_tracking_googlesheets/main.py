import requests
from datetime import datetime
import os
APP_ID = os.environ.get('APP_ID')
# APP_KEY = '5bb7533ea3e857ca6e4f8997f3b4b04b'
APP_KEY = os.environ.get('APP_KEY')
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
# sheet_endpoint = 'https://api.sheety.co/2c8433cf6652605fe15aa4d28a77294d/pythonLearning/workouts'
sheet_endpoint = os.environ.get('SHEET_ENDPOINT')
API_HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}
# exercise_text = input('Tell me which exercises you did: ')
request_body = {
    'query': 'Running 3 miles',
    'gender': 'male',
    'weight_kg': 90,
    'height_cm': 188,
    'age': 30
}

response = requests.post(url=exercise_endpoint, json=request_body, headers=API_HEADERS, )
response.raise_for_status()
result = response.json()

post_date = datetime.today().strftime('%d/%m/%Y')
post_time = datetime.now().strftime('%H:%M:%S')
sheet_header = {
    "Authorization": 'Bearer 5bb7533ea3e857ca6e4f8997f3b4b04b'
}
for exercise in result['exercises']:
    sheet_inputs = {
        'workout': {
            'date': post_date,
            'time': post_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=sheet_header)
    print(sheet_response.text)
