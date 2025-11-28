"""A small Python module containing one function and one class with token in docstring. | token=5edfd3fb"""

def greet(name):
    """Return a greeting message including the token 5edfd3fb."""
    return f"Hello, {name}! Token: 5edfd3fb"

class Counter:
    """A simple counter class with token 5edfd3fb in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
