                                                        # Exercise 9-1-solution

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
# for grades in student_scores:
#     if student_scores[grades] >= 91:
#         student_grades[grades] = 'Outstanding'
#     elif 81 <= student_scores[grades] <= 90:
#         student_grades[grades] = 'Exceeds Expectations'
#     elif 71 <= student_scores[grades] <= 80:
#         student_grades[grades] = 'Acceptable'
#     else:
#         student_grades[grades] = 'Fail'
# 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = {
#     'France': {
#         'cities_visited': ['Paris', 'Lille', 'Dijon'],
#         'Total visits': 12
#     },
#     'Germany': {
#         'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
#         'Total visits': 5
#     }
# }

# travel_log = [
#     {
#         'country': 'France',
#         'cities_visited': ['Paris', 'Lille', 'Dijon'],
#         'total_visits': 12
#     },
#     {
#         'country': 'Germany',
#         'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
#         'Total visits': 5
#     }
# ]

                                                        # Exercise 9.2 add new dict to nested list

# travel_log = [
#     {
#       "country": "France",
#       "visits": 12,
#       "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#       "country": "Germany",
#       "visits": 5,
#       "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


# def add_new_country(country, visits, cities):
#     new_dict = {
#         'country': country,
#         'visits': visits,
#         'cities': cities
#     }
#     travel_log.append(new_dict)


#🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

                                                        # Exercise 9.3 Day project. Secret auction
import os
from art import logo
auction_participants = {}
auction_is_going = True
print(logo)
while auction_is_going:
    name = input('What\'s your name? ')
    bid = int(input('What\'s your bid? '))
    other_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'').lower()
    auction_participants[name] = bid
    if other_bidders == 'yes':
        os.system('clear')
    if other_bidders == 'no':
        os.system('clear')
        auction_is_going = False

max_bid = max(auction_participants)
print(auction_participants)
print(f'The winner is {max_bid} with a bid of ${auction_participants[max_bid]}')
