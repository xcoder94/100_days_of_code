from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


def higher_lower_decorator(fn):
    def wrapper():
        pass
    return wrapper

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="http://surl.li/orpno" style="width:600px">')


# Different routes using the app.rout decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye'


# Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/1')
def greet(name):
    return f'Hello {name}'


@app.route('/<int:number>')
def greet(number):
    return f'Hello {number}'


if __name__ == '__main__':
    # Run the app in debug mode to auto reload
    app.run(debug=True)
