#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"

@app.route('/airbnb-onepage/')
def alxbnb():
    return "alX-Airbnb_clone_v2!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
