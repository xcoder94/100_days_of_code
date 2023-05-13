# import csv

# with open('./weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv('./weather_data.csv')
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)


# print(data['temp'].mean())
# print(data['temp'].max())

# Get data in columns
# print(data['conditions'])
# print(data.condition)

# Get data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data['temp'].max()])
# monday = data[data.day == 'Monday']
# print(monday.condition)
# monday_temp_in_farinhate = monday.temp * 1.8 + 32
# print(monday_temp_in_farinhate)


# Create a data frame from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv('new_data.csv')

data = pandas.read_csv('./Squirrel_Data.csv')
















