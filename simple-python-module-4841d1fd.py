"""A small Python module containing one simple function and one simple class with the token '4841d1fd' included in a docstring. | token=4841d1fd"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 4841d1fd."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
