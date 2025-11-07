"""A small Python module with one function and one class, including a specific token in a docstring. | token=787a42c9"""

def greet(name):
    """Return a greeting message including the token 787a42c9."""
    return f"Hello, {name}! This is token 787a42c9."

class Counter:
    """A simple counter class with token 787a42c9 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
