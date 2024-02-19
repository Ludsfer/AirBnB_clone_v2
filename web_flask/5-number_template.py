#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """displays 'C' followed by the value of <text>"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    """displays 'Python' followed by a <text> input"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """ displays 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
