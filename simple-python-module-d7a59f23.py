"""A small Python module with one function and one class, including a specific token in the docstring. | token=d7a59f23"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class with token d7a59f23 included."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
