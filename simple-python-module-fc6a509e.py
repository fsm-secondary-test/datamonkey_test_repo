"""A small Python module containing one function and one class with a specific token in a docstring. | token=fc6a509e"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class that increments a value. Token: fc6a509e"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
