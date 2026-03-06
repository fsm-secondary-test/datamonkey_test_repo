"""A small Python module with one function and one class including a token in a docstring. | token=f28f50e7"""

def greet(name):
    """Return a greeting message including the token f28f50e7."""
    return f"Hello, {name}! Token: f28f50e7"

class Counter:
    """A simple counter class with token f28f50e7 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def value(self):
        """Return the current count."""
        return self.count
