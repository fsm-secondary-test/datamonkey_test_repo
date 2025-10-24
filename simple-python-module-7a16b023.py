"""A small Python module containing one simple function and one simple class. Includes the literal token '7a16b023' in a docstring. | token=7a16b023"""

def greet(name):
    """Return a greeting message including the name provided."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 7a16b023 included in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
