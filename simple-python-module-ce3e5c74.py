"""A small Python module with one function and one class, including a specific token in the docstring. | token=ce3e5c74"""

def greet(name):
    """Return a greeting message including the token ce3e5c74."""
    return f"Hello, {name}! Token: ce3e5c74"

class Counter:
    """Simple counter class with token ce3e5c74."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
