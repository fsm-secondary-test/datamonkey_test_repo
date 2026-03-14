"""A small Python module with one function and one class. Includes the token 'dea0bfef' in a docstring. | token=dea0bfef"""

def greet(name):
    """Return a greeting message including the token dea0bfef."""
    return f"Hello, {name}! Token: dea0bfef"

class Counter:
    """Simple counter class that increments a count."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def value(self):
        """Return the current count."""
        return self.count
