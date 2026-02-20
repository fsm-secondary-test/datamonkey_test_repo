"""A small Python module with one function and one class, including a literal token in a docstring. | token=2ff2a4a1"""

def greet(name):
    """Return a greeting message including the token 2ff2a4a1."""
    return f"Hello, {name}! Token: 2ff2a4a1"

class Counter:
    """A simple counter class that uses token '2ff2a4a1' in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
