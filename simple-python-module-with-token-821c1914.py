"""A small Python module containing one function and one class. The module includes the literal token '821c1914' in a docstring. | token=821c1914"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class Person:
    """Person class holding a name and a token '821c1914'."""

    TOKEN = '821c1914'

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I'm {self.name}. My token is {self.TOKEN}."
