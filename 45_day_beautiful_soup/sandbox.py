from bs4 import BeautifulSoup
import requests


with open('website.html', 'r') as content:
    soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())

# print(soup.title)  # Html title tag with content
# print(soup.title.string)  # Html title tag's content without tag name
# print(soup.p)  # Html p tag with inner tags and contents

all_a_tags = soup.find_all(name='a')  # Finds and returns all a tags
# print(all_a_tags)

# for tag in all_a_tags:
#     print(tag.getText())  # returns only tag's content
#     print(tag.get('href'))  # returns only tag's link

heading = soup.find(name='h1', id='name')  # finds and returns h1 tag that owned id
section_heading = soup.find(name='h3', class_='heading')  # finds and returns h1 tag that owned this class name
# print(section_heading)

company_url = soup.select_one(selector='p a')  # select by tag name in tree
name = soup.select_one(selector='#name')  # select by ID name in tree
headings = soup.select('.heading')  # select by class name in tree
print(headings)

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all('a', attrs={'rel': 'noreferrer'})
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

# print(article_texts)
# print(article_links)
# print(article_upvotes)
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])