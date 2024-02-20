from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

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
bootstrap = Bootstrap5(app)
# all_books = []


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add book')


class EditForm(FlaskForm):
    new_rating = StringField('New Rating', validators=[DataRequired()])
    submit = SubmitField('Change Rating')


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        book_db = result.scalars().all()
        print(book_db)
    return render_template('index.html', all_books=book_db)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    book_to_edit = None
    result = db.session.execute(db.select(Book).order_by(Book.title))
    book_db = result.scalars().all()
    for book in book_db:
        if book.id == index:
            book_to_edit = book
    form = EditForm()
    if form.validate_on_submit():
        book_id = index
        with app.app_context():
            # book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
            book_to_update = db.get_or_404(Book, book_id)
            book_to_update.rating = form.new_rating.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", book=book_to_edit, form=form)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # new_book = {
        #     'title': form.book_name.data,
        #     'author': form.book_author.data,
        #     'rating': int(form.rating.data)
        # }
        # all_books.append(new_book)
        new_book = Book(title=form.book_name.data, author=form.book_author.data, rating=int(form.rating.data))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
