"""A small Python module containing one simple function and one simple class. Includes the token '5f9f55ac' in a docstring. | token=5f9f55ac"""

def greet(name):
    """Return a greeting message with the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class that includes token 5f9f55ac in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count."""
        return self.count
