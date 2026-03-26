"""A small Python module with one function and one class, including a token in a docstring. | token=15ae2718"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 15ae2718 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
