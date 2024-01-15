#!/usr/bin/python3
"""Module that starts a Flask web application and defines some routes"""
from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """Routes to HTML page"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Handles closing of the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
