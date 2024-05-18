#!/usr/bin/python3
"""flask starter"""

from flask import Flask, render_template

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
    """
    Replaces underscores in the input text with spaces and prepends 'C '
    to the modified text.
    """

    modified_text = text.replace("_", " ")
    return f"C {modified_text}"


@flask.route("/python/<text>", strict_slashes=False)
@flask.route("/python", strict_slashes=False)
def route_python(text="is cool"):
    """
    Renders a string that says "Python {text}",
    where {text} is the provided text with underscores replaced by spaces.
    """

    text = text.replace("_", " ")
    return f"Python {text}"


@flask.route("/number/<int:n>")
def route_num(n):
    """
    Returns a string indicating that the given number is a number.
    """

    return f"{n} is a number"


@flask.route('/number_template/<int:n>', strict_slashes=False)
def num(n):
    """Display HTML only if n is an integer."""
    return render_template('5-number.html', n=n)


@flask.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """
    Renders a template that displays whether the given number is odd or even.
    """

    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    flask.run(host="0.0.0.0", port=5000)
