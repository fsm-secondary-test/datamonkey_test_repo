"""A small Python module with one function and one class, including a token in a docstring. | token=38f25c04"""

def greet(name):
    """Return a greeting message including token 38f25c04."""
    return f"Hello, {name}! Your token is 38f25c04."

class Counter:
    """Simple counter class with token 38f25c04."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
