"""A small Python module containing one simple function and one simple class. The module includes the literal token '9b39b9c9' in a docstring. | token=9b39b9c9"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class that increments a count.

    Token: 9b39b9c9
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
