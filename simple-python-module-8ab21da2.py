"""A small Python module with one function and one class, including a specific token in a docstring. | token=8ab21da2"""

def greet(name):
    """Return a greeting message including the token 8ab21da2."""
    return f"Hello, {name}! Your token is 8ab21da2."

class Counter:
    """A simple counter class that uses token 8ab21da2 internally."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
