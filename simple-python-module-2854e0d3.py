"""A small Python module containing one simple function and one simple class, including a specific token in a docstring. | token=2854e0d3"""

def greet(name):
    """Return a greeting message including the token 2854e0d3."""
    return f"Hello, {name}! Your token is 2854e0d3."

class Counter:
    """Simple counter class with token 2854e0d3."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
