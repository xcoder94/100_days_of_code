import random

# random_integer = random.randint(1, 10)
# print(random_integer)


# random_float = random.random()
# random_0_5 = random.random() * 5
# print(random_0_5)

                                                        # Heads or trails
# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
# heads_or_trails = random.randint(0, 1)
# if heads_or_trails:
#     print('Heads')
# else:
#     print('Tails')

                                                        # Banker Roulette
# Import the random module here

# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# will_pay = random.randint(1, len(names) + 1)
# print(f'{names[will_pay]} is going to buy the meal today!')

                                                        # nested lists
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[1][2])
# # print(dirty_dozen[1][3])
# print(dirty_dozen[1][1])

                                                        # Tresure map

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# Angelas code
# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical - 1][horizontal - 1] = "X"
# My Code
# if int(position) == 11:
#     row1[0] = 'X'
# if int(position) == 21:
#     row1[1] = 'X'
# if int(position) == 31:
#     row1[2] = 'X'
# if int(position) == 12:
#     row2[0] = 'X'
# if int(position) == 22:
#     row2[1] = 'X'
# if int(position) == 32:
#     row2[2] = 'X'
# if int(position) == 13:
#     row3[0] = 'X'
# if int(position) == 23:
#     row3[1] = 'X'
# if int(position) == 33:
#     row3[2] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

                                                        # Rock paper scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
#Write your code below this line 👇
user_choice = input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n')
computer_choice = random.randrange(3)
if int(user_choice) == 0 and computer_choice == 2:
    print('Your choice')
    print(images[int(user_choice)])
    print('Comp choice')
    print(images[computer_choice])
    print('You win')
elif int(user_choice) == 0 and computer_choice == 1:
    print('Your choice')
    print(images[int(user_choice)])
    print('Comp choice')
    print(images[computer_choice])
    print('You Loose')

elif int(user_choice) == 1 and computer_choice == 0:
    print('Your choice')
    print(images[int(user_choice)])
    print('Comp choice')
    print(images[computer_choice])
    print('You win')
elif int(user_choice) == 1 and computer_choice == 2:
    print('Your choice')
    print(images[int(user_choice)])
    print('Comp choice')
    print(images[computer_choice])
    print('You Loose')

elif int(user_choice) == 2 and computer_choice == 1:
    print('Your choice')
    print(images[int(user_choice)])
    print('Comp choice')
    print(images[computer_choice])
    print('You win')
elif int(user_choice) == 2 and computer_choice == 0:
    print('Your choice')
    print(images[int(user_choice)])
    print('Comp choice')
    print(images[computer_choice])
    print('You Loose')
else:
    print('Your choice')
    print(images[int(user_choice)])
    print('Comp choice')
    print(images[computer_choice])
    print('Its draw')