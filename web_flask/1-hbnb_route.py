#!/usr/bin/python3
"""Module that starts a Flask web application and defines some routes"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Routes to home page"""
    return "Hello HBNB!"


@app.route("/hbnb/")
def hbnb():
    """Routes to hbnb page"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
