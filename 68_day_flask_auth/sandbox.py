from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask
from sqlalchemy import Integer, String


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

with app.app_context():
    users_list = db.session.execute(db.select(User).order_by(User.id)).scalars()

for i in users_list:
    print(i)
