from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

search_url = "https://api.themoviedb.org/3/search/movie"
details_url = 'https://api.themoviedb.org/3/movie'
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjY2NlNGNhMDQ1MDFmMGE3NjczNzlhNmNkNDZhNjg5NSIsInN1YiI6IjY1ZGYwZWU1YjM5ZTM1MDE2MzJmOWVlZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pcKqyzqB2JuqXfIQEtpKJAPHT8eBPnoH44PitqSEF1Y"
}


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class RateMovieForm(FlaskForm):
    rating = StringField('Your rating out 10 e.g 7.5', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')


class FindMovieForm(FlaskForm):
    movie_title = StringField('Movie title', validators=[DataRequired()])
    submit = SubmitField('Add movie')


with app.app_context():
    db.create_all()

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()


@app.route('/')
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    print(all_movies)

    return render_template('index.html', movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        params = {
            'query': form.movie_title.data,
            'include_adult': False,
            'include_video': False,
            'language': 'en-US',
            'page': 1,
            'sort_by': 'popularity.desc'

        }
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        movies_data = response.json()['results']
        return render_template('select.html', movies=movies_data)
    return render_template('add.html', form=form)


@app.route('/find')
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f'{details_url}/{movie_api_id}'
        response = requests.get(movie_api_url, params={'language': 'en-US'}, headers=headers)
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{movie_api_url}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


@app.route('/edit', methods=['GET', 'POST'])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
