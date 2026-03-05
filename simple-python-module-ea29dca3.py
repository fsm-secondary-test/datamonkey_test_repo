"""A small Python module with one function and one class including a specific token in a docstring. | token=ea29dca3"""

def greet(name):
    """Return a greeting message including the token ea29dca3."""
    return f"Hello, {name}! This message includes token ea29dca3."

class Counter:
    """Simple counter class with token ea29dca3 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
