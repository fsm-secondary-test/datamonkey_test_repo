"""A small Python module containing one simple function and one simple class. Includes the literal token '050c57b6' in a docstring. | token=050c57b6"""

def greet(name):
    """Return a greeting message. Token: 050c57b6"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 050c57b6."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
