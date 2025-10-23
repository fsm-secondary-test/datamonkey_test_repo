"""A small Python module with one function and one class, including a specific token in a docstring. | token=bb347403"""

def greet(name):
    """Return a greeting message including the token bb347403."""
    return f"Hello, {name}! Token: bb347403"

class Counter:
    """A simple counter class that tracks counts. Token: bb347403"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
