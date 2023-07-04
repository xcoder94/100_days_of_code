import pandas
import random


# Data
data = pandas.read_csv('data/french_words.csv')
data_to_dict = pandas.DataFrame.to_dict(data, orient='records')


def random__french_word():
    random_word = random.choice(data_to_dict)
    print(random_word['French'])


random__french_word()