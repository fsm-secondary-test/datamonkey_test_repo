"""A small Python module containing one function and one class, including the token 'bc586251' in a docstring. | token=bc586251"""

def greet(name):
    """Return a greeting message including the token bc586251."""
    return f"Hello, {name}! This is token bc586251."

class Counter:
    """A simple counter class that stores the token bc586251 as a class attribute."""

    token = 'bc586251'

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
