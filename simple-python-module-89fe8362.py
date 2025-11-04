"""A simple Python module containing one function and one class with a specific token in the docstring. | token=89fe8362"""

def greet(name):
    """Return a greeting message including the 89fe8362 token."""
    return f"Hello, {name}! Token: 89fe8362"

class Counter:
    """A simple counter class with token 89fe8362 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
