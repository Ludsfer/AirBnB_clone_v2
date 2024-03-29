#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ display 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ display 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ display char C followed by a text input """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ display Python, with a given text input, default
    value of text: is cool """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ number route """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
