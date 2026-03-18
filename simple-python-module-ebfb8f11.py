"""A small Python module with one function and one class, including a specific token in a docstring. | token=ebfb8f11"""

def greet(name):
    """Return a greeting message including the token ebfb8f11."""
    return f"Hello, {name}! Token: ebfb8f11"

class Counter:
    """A simple counter class that uses token ebfb8f11 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
