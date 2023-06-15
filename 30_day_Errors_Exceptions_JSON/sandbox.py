# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key': 'Value'}
#     print(a_dictionary['key'])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('something')
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist.')
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print('File was closed')
#     raise TypeError('This is an error that I made up')


# height = float(input('Height: '))
# weight = float(input('Weight: '))

# if height > 3:
#     raise ValueError('Human height should not be over 3 meters')


# Code exercise 1
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('Fruit pie')
    else:
        print(fruit + " pie")


make_pie(4)


# Code exercise 2
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass


# print(total_likes)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()