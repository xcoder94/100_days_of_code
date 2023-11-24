import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage_html = response.text
soup = BeautifulSoup(webpage_html, 'html.parser')

films_headings = soup.find_all(name='h3', class_='listicleItem_listicle-item__title__hW_Kn')
all_films_list = [films.getText() for films in films_headings]
sorted_list = list(reversed(all_films_list))
with open('movies.txt', 'w') as file:
    for films in sorted_list:
        file.write(f'{films}\n')
print(sorted_list)
