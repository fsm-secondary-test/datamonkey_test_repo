"""A small Python module with one function and one class, including a specific token in a docstring. | token=ec4133ea"""

def greet(name):
    """Return a greeting message including the token ec4133ea."""
    return f"Hello, {name}! Token: ec4133ea"

class Counter:
    """A simple counter class that uses token ec4133ea internally."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
