#!/usr/bin/python3
"""flask starter"""

from flask import Flask


flask = Flask(__name__)


@flask.route("/", strict_slashes=False)
def hello_HBNB():
    """
    Returns the string "Hello HBNB!" when the /hello_HBNB route is accessed.
    """

    return "Hello HBNB!"


@flask.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Renders the "HBNB" string in response to a GET request to the "/hbnb".
    """

    return "HBNB"


@flask.route("/c/<text>", strict_slashes=False)
def dynamic_route(text):
    modified_text = text.replace("_", " ")
    return f'C {modified_text}'


if __name__ == '__main__':
    flask.run(host='0.0.0.0', port=5000)
