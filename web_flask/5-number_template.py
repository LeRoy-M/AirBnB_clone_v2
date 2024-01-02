#!/usr/bin/python3
"""Module that starts a Flask web application and defines some routes"""
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Routes to home page"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Routes to hbnb page"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """Routes to C `comment` page"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python_text(text):
    """Routes to Python `comment` page"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>")
def number(n):
    """Routes to number `integer` page"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def num_templ(n):
    """Routes number urls to a template page"""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
