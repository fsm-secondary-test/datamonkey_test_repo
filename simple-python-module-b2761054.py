"""A small Python module with one function and one class including a specific token in a docstring. | token=b2761054"""

def greet(name):
    """Return a greeting message including the token b2761054."""
    return f"Hello, {name}! Token: b2761054"

class Counter:
    """A simple counter class with token b2761054 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
