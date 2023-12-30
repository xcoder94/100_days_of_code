from flask import Flask
import random
app = Flask(__name__)

rand_number = random.randint(0, 9)


@app.route('/')
def main_page():
    return ('<h1>Guess the number between 0 and 9</h1>'
            '<img src="http://surl.li/osgxi" style="width:600px">')


@app.route('/<int:number>')
def guess_page(number):
    if number > rand_number:
        return ('<h1>Too high, try again !</h1>'
                '<img src="http://surl.li/osvjv" style="width:600px">')
    elif number < rand_number:
        return ('<h1>Too low, try again !</h1>'
                '<img src="http://surl.li/osvkm" style="width:600px">')
    else:
        return ('<h1>You found me!</h1>'
                '<img src="http://surl.li/osvkv" style="width:600px">')


@app.route('/<int:number>')
def greet(number):
    return f'Hello {number}'


if __name__ == '__main__':
    # Run the app in debug mode to auto reload
    app.run(debug=True)
