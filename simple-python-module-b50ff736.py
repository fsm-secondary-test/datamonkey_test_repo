"""A small Python module with one function and one class, including a token in a docstring. | token=b50ff736"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token b50ff736 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
