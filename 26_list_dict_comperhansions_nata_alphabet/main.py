import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    # print(key, value)

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    # if row.student == 'Angela':
    #     print(row['score'])

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabet_file = pandas.read_csv('./nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet_file.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input('Enter your name: ').upper()
name_symbols = [symbols for symbols in user_name]
# print(name_symbols)
phonetic_code_words = [nato_dict[letter] for letter in user_name]
print(phonetic_code_words)
