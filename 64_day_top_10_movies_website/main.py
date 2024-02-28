from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
url = "https://api.themoviedb.org/3/discover/movie"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjY2NlNGNhMDQ1MDFmMGE3NjczNzlhNmNkNDZhNjg5NSIsInN1YiI6IjY1ZGYwZWU1YjM5ZTM1MDE2MzJmOWVlZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pcKqyzqB2JuqXfIQEtpKJAPHT8eBPnoH44PitqSEF1Y"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies_list.db'
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


with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class NewFilmForm(FlaskForm):
    new_film = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add')


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()


@app.route('/')
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars()
    return render_template('index.html', movies=all_movies)


# Adding the Update functionality
@app.route('/edit', methods=['GET', 'POST'])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
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


@app.route('/add')
def add():
    form = NewFilmForm()
    return render_template('add.html', form=form)


@app.route('/select')
def select():
    params = {
        'include_adult': False,
        'include_video': False,
        'language': 'en-US',
        'page': 1,
        'sort_by': 'popularity.desc'

    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()['results']
    return render_template('select.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
