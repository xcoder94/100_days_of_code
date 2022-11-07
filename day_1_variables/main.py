# Printing
print("Day 1 - Python Print Function \nThe function is declared like this: \nprint('what to print')")

# Debugging
print("Day 1 - String Manipulation")
print("String Concatenation is done with the " + " sign.")
print("e.g. print('Hello ' + 'world')")
print("New lines can be created with a backslash and n.")

# Input functions
name_len = input('What is your name? ')
print(len(name_len))

# Variables
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Day 1 project band name generator
#Go to: https://replit.com/@appbrewery/band-name-generator-start?v=1
#1. Create a greeting for your program.
print('Welcome to the band name generator.')
#2. Ask the user for the city that they grew up in.
city_name = input('What\'s name of the city you grew up in?\n')
#3. Ask the user for the name of a pet.
pet_name = input('What\'s pet\'s name?\n')
#4. Combine the name of their city and pet and show them their band name.
print('Your band name could be ' + city_name + ' ' + pet_name)
#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end