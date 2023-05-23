import random
numbers = [1, 2, 3]
new_numbers = [new_item + 1 for new_item in numbers]
# print(new_numbers)


name = 'Angela'
new_list = [letter for letter in name]
# print(new_list)

doubled_nums = [nums * 2 for  nums in range(1, 5)]
# print(doubled_nums)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Fraddie']
short_names = [name for name in names if len(name) < 5]
# print(short_names)

uppered_long_names = [name.upper() for name in names if len(name) > 5]
# print(uppered_long_names)


# Exercise 1 - Squaring Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [num ** 2 for num in numbers]

#Write your code 👆 above:

# print(squared_numbers)

# Exercise 2 - Filtering Even Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

#Write your code 👆 above:

# print(result)


# Exercise 3 - Data Overlap
with open('./file1.txt') as f1, open('./file2.txt') as f2:
    # convert readed content into list
    f1_content = [int(line.strip()) for line in f1]
    f2_content = [int(line.strip()) for line in f2]

# print(f'File 1 numbers {f1_content}')
# print(f'File 2 numbers {f2_content}')
result = [num for num in f1_content if num in f2_content]
# Write your code above 👆

# print(result)


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Fraddie']
student_score = {student:random.randint(1, 100) for student in names}
print(student_score)

passed_students = {}