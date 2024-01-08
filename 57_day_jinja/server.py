from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<some_name>')
def guess_page(some_name):
    age_response = requests.get(f'https://api.agify.io?name={some_name}')
    age_response.raise_for_status()
    person_age = age_response.json()['age']
    gender_response = requests.get(f'https://api.genderize.io?name={some_name}')
    gender_response.raise_for_status()
    person_gender = gender_response.json()['gender']
    return render_template('guess.html', person_name=some_name, person_gender=person_gender, person_age=person_age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    fake_blog_url = 'https://api.npoint.io/9da5abbbe295fea03dee'
    blog_response = requests.get(fake_blog_url)
    all_posts = blog_response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
