"""A small Python module with one function and one class, including a specific token in a docstring. | token=6c10b27c"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """SimpleCounter class with token 6c10b27c in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
