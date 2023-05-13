                                                    # Ex 1 Data types
# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[-1])
# answer = first_digit + second_digit
# print(answer)

                                                    # Math operations
# print(3 * (3 + 3) / 3 - 3)

# BMI Calculating
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# BMI = weight / (height ** 2)
# print(round(BMI))

                                                    # Life in days, weeks, month
# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# life_in_days = 90 * 365
# life_in_weeks = 90 * 52
# life_in_month = 90 * 12
# have_days = life_in_days - int(age) * 365
# have_weeks = life_in_weeks - int(age) * 52
# have_month = life_in_month - int(age) * 12
# print(f'You have {have_days} days, {have_weeks} weeks, and {have_month} months left.')

                                                    # Tip calculator
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? '))
percentage_of_bill = float(input('What percentage tip would yoi like to give? '))
num_of_people = int(input('How many people to split the bill? '))
bill_to_each = (total_bill + total_bill / 100 * percentage_of_bill)/ num_of_people
print(f'Each person should pay {bill_to_each}')
