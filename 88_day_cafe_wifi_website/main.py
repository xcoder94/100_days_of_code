from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdsadasd1e12e1e2e2133v1122eewqe0'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafes(db.Model):
    __tablename__ = 'cafe'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(), nullable=False)
    img_url: Mapped[str] = mapped_column(String(), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Integer, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Integer, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Integer, nullable=False)
    seats: Mapped[str] = mapped_column(String(), nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(), nullable=False)


with app.app_context():
    db.create_all()


@app.template_filter('bool_to_str')
def bool_to_str(value):
    return 'Yes' if value else 'No'


app.jinja_env.filters['bool_to_str'] = bool_to_str


@app.route('/')
def get_all_cafes():
    result = db.session.execute(db.select(Cafes))
    cafes = result.scalars().all()
    return render_template('index.html', all_cafes=cafes)


@app.route('/cafe/<int:cafe_id>')
def show_cafe(cafe_id):
    requested_cafe = db.get_or_404(Cafes, cafe_id)
    if not requested_cafe:
        return "Cafe not found", 404
    return render_template('cafe.html', cafe=requested_cafe)


if __name__ == '__main__':
    app.run(debug=True)
