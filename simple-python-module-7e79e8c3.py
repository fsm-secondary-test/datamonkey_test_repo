"""A small Python module with one function and one class, including a token in a docstring. | token=7e79e8c3"""

def greet(name):
    """Return a greeting message including the token 7e79e8c3."""
    return f"Hello, {name}! Token: 7e79e8c3"

class Counter:
    """Simple counter class with token 7e79e8c3 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
