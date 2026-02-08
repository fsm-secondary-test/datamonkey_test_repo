"""A Python module with one function and one class, including a literal token in a docstring. | token=3a9fe383"""

def greet(name):
    """Return a greeting message including the token 3a9fe383."""
    return f"Hello, {name}! Your token is 3a9fe383."

class Counter:
    """Simple counter class with token 3a9fe383 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
