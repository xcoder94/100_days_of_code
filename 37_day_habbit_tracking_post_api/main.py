import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'pytonstudent'
TOKEN = 'kjhfkajhbkjqe1eh230983jndfkjd'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# create_user = requests.post(url=pixela_endpoint, json=user_params)
# print(create_user.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graphs_config = {
    'id': 'graphs1',
    'name': 'Coding Graphs',
    'unit': 'Hours',
    'type': 'float',
    'color': 'shibafu'
}
headers = {
    'X-USER-TOKEN': TOKEN
}

# create_graphs = requests.post(url=graph_endpoint, json=graphs_config, headers=headers)
post_pixel_endpoint = f'{graph_endpoint}/graphs1'
past_days = datetime(year=2023, month=11, day=6)
today = datetime.now()
post_pixel_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many hours you coded today? '),
}
create_pixel = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(create_pixel.text)

update_pixel_endpoint = f'{post_pixel_endpoint}/{past_days.strftime("%Y%m%d")}'
graphs_update = {
    'quantity': '2.5'
}
# update_pixel_put = requests.put(url=update_pixel_endpoint, json=graphs_update, headers=headers)
# print(update_pixel_put.text)

# delete_pixel = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(delete_pixel)


