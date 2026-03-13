"""A small Python module with one function and one class, including a literal token in a docstring. | token=7bf9436a"""

def greet(name):
    """Return a greeting message including the token 7bf9436a."""
    return f"Hello, {name}! Token: 7bf9436a"

class Counter:
    """A simple counter class with token 7bf9436a in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
