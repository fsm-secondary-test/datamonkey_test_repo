"""A small Python module with one function and one class including a specific token in the docstring. | token=fd21b357"""

def greet(name):
    """Return a greeting message including the token fd21b357."""
    return f"Hello, {name}! Token: fd21b357"

class Counter:
    """Simple counter class that counts upwards. Token: fd21b357"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
