"""A small Python module with one function and one class, including a specific token in a docstring. | token=ca6f310d"""

def greet(name):
    """Return a greeting message including the provided name. Token: ca6f310d"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class. Token: ca6f310d"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
