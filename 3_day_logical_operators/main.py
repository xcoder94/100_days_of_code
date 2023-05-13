                                                        # 3.1 exercise Odd or even
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# if number % 2 > 0:
#     print('This is an odd number.')
# else:
#     print('This is an even number.')

                                                        # BMI 2.0
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# BMI = weight / (height ** 2)
# if 18.5 > BMI:
#     print(f'Your BMI is {round(BMI, 2)}, you are underweight.')
# elif 18.5 < BMI < 25:
#     print(f'Your BMI is {round(BMI, 2)}, you have a normal weight.')
# elif 25 < BMI < 30:
#     print(f'Your BMI is {round(BMI, 2)}, you are slightly overweight.')
# elif 30 < BMI < 35:
#     print(f'Your BMI is {round(BMI, 2)}, you are obese.')
# else:
#     print(f'Your BMI is {round(BMI, 2)}, you are clinically obese.')

                                                        # leap Year

# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Leap year.')
#         else:
#             print('Not a leap year')
#     else:
#         print('Leap year')
# else:
#     print('Not a leap year')

                                                        # Pizza order practice
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# pizza_bill = 0
# pepperoni_bill = 0
# extra_cheese_bill = 0
# if size.upper() == 'S':
#     pizza_bill = 15
# if size.upper() == 'M':
#     pizza_bill = 20
# if size.upper() == 'L':
#     pizza_bill = 25
# if add_pepperoni.upper() == 'Y' and size.upper() == 'S':
#     pepperoni_bill = 2
# if add_pepperoni.upper() == 'Y' and size.upper() != 'S':
#     pepperoni_bill = 3
# if extra_cheese.upper() == 'Y':
#     extra_cheese_bill = 1
# total_bill = pizza_bill + pepperoni_bill + extra_cheese_bill
#
# print(f'Your final bill is: ${total_bill}')

                                                        # Love score
# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
#
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")

                                                        # Tresure island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_choice = input('You have to choose one way Left or Right? \n')
if first_choice.lower() != 'left':
    print('Fall into a hole. Game over')
else:
    lake = input('You have to came lake. What will you do? Swim or wait?\n ')
    if lake.lower() != 'wait':
        print('Attacked by trout. Game over')
    else:
        come_a_cross_to_house = input('You found a house. The house has 3 doors. Red, Yellow and Blue. Which door you '
                                      'will enter? \n')
        if come_a_cross_to_house.lower() == 'red':
            print('Burned by fire. Game over')
        elif come_a_cross_to_house.lower() == 'blue':
            print('Eaten by beasts. Game over')
        elif come_a_cross_to_house.lower() == 'yellow':
            print('You win')
        else:
            print('Game over you lose')