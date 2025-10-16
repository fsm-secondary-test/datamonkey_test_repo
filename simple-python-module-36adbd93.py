"""A small Python module containing one function and one class with a specific token in the docstring. | token=36adbd93"""

def greet(name):
    """Return a greeting message including the token 36adbd93."""
    return f"Hello, {name}! (token: 36adbd93)"

class Counter:
    """A simple counter class that uses token 36adbd93 in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current value of the counter."""
        return self.count
