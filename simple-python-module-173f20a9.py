"""A small Python module containing one function and one class with a specific token in the docstring. | token=173f20a9"""

def greet(name):
    """Return a greeting message including the token 173f20a9."""
    return f"Hello, {name}! Your token is 173f20a9."

class Counter:
    """A simple counter class with token 173f20a9 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
