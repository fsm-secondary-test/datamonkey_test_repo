"""A small Python module with one function and one class, including the token '4278dac0' in a docstring. | token=4278dac0"""

def greet(name):
    """Return a greeting message including the token 4278dac0."""
    return f"Hello, {name}! Your token is 4278dac0."

class Counter:
    """Simple counter class that counts up from zero. Token: 4278dac0"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
