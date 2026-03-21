"""A small Python module with one function and one class. | token=1c968798"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 1c968798."""
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
        return self.count
