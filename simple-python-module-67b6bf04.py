"""A small Python module with one function and one class, including a specific token in the docstring. | token=67b6bf04"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 67b6bf04 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
