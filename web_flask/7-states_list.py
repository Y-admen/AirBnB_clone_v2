#!/usr/bin/python3
"""
A script to To load all cities of a State,
If storage engine is DBStorage, use cities relationship
Otherwise, use the public getter method cities.
After each request remove the current SQLAlchemy Session,
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/cities_by_states: display a HTML page: (inside the tag BODY)
H1 tag: “States”

"""
from flask import Flask, render_template
from models import storage
from models.state import State


flask = Flask(__name__)


@flask.route("/", strict_slashes=False)
def hello_HBNB():
    """
    Returns the string "Hello HBNB!" when the /hello_HBNB route is accessed.
    """

    return "Hello HBNB!"


@flask.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@flask.teardown_appcontext
def teardown_db(ctx):
    storage.close()


if __name__ == "__main__":
    flask.run(host='0.0.0.0', port=5000)
