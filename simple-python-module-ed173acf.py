"""A small Python module containing one function and one class, with a specific token in the docstring. | token=ed173acf"""

def greet(name):
    """Return a greeting message including the token ed173acf."""
    return f"Hello, {name}! This is token ed173acf."

class Counter:
    """Simple counter class that uses token ed173acf in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
