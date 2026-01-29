"""A small Python module with one function and one class including a specific token in a docstring. | token=27cc42b4"""

def greet(name):
    """Return a greeting message including the token 27cc42b4."""
    return f"Hello, {name}! Token: 27cc42b4"

class Counter:
    """A simple counter class. Token: 27cc42b4"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
