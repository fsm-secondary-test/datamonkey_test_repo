"""A Python module containing one simple function and one simple class, including a specific token in the docstring. | token=cccb8430"""

def greet(name):
    """Return a greeting message with the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token cccb8430."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
