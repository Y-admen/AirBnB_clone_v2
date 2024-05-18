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


if __name__ == '__main__':
    flask.run(host='0.0.0.0', port=5000)
