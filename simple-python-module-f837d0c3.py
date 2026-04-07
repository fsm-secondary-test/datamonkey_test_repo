"""A small Python module containing a simple function and a simple class, including the literal token 'f837d0c3' in a docstring. | token=f837d0c3"""

def greet(name):
    """Return a greeting message including the token f837d0c3."""
    return f"Hello, {name}! Your token is f837d0c3."

class SimpleCounter:
    """A simple counter class that counts up from zero. Token: f837d0c3"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
