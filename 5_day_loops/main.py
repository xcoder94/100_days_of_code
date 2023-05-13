                                                        # 5.1 exercise 1 Average Height
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# student_heights = [156, 178, 165, 171, 187]
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# sum_of_height = 0
# len_of_heights = 0
# for i in student_heights:
#     sum_of_height += i
#     len_of_heights += 1
#
# average_of_heights = round(sum_of_height / len_of_heights)
# print(average_of_heights)

                                                        # 5.2 exercise 2 High score

# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# high_score = 0
# for i in student_scores:
#     if i > high_score:
#         high_score = i
#     else:
#         pass
#
# print(f'The highest score in the class is: {high_score}')

                                                        # 5.3 exercise 3 Adding even numbers
#Write your code below this row 👇

# even_sum = 0
# for even in range(1, 101):
#     if even % 2 == 0:
#         print(f'{even_sum} + {even}')
#         even_sum += even
#     else:
#         pass
# print(even_sum)

                                                        # 5.4 exercise 4 Fizz buzz game
#Write your code below this row 👇

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 > 0:
#         print('Fizz')
#     elif num % 5 == 0 and num % 3 > 0:
#         print('Buzz')
#     elif num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     else:
#         print(num)


                                                        # Day 5 project random pass generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generated_pass = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(1, nr_letters + 1):
    generated_pass += random.choice(letters)

for i in range(1, nr_symbols + 1):
    generated_pass += random.choice(symbols)

for i in range(1, nr_numbers + 1):
    generated_pass += random.choice(numbers)

print(generated_pass)
random.shuffle(generated_pass)
generated_pass = ' '.join(generated_pass)
print(generated_pass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P




