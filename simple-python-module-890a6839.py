"""A small Python module with one function and one class, including a specific token in a docstring. | token=890a6839"""

def greet(name):
    """Return a greeting message including the given name and token 890a6839."""
    return f"Hello, {name}! This is token 890a6839."

class Counter:
    """A simple counter class that counts up from zero. Token: 890a6839"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
