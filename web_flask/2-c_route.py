#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display 'Hello HBNB'"""
    return "Hello HBNB"


@app.route('/hbnb')
def hbnb():
    """display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def text(text):
    """display simple text"""
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
