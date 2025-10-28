"""A small Python module containing one function and one class, with a unique token in the docstring. | token=e5d85430"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token e5d85430 in docstring."""
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count
