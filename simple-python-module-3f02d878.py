"""A small Python module with one function and one class. Includes a literal token in a docstring. | token=3f02d878"""

def greet(name):
    """Return a greeting message including the token 3f02d878."""
    return f"Hello, {name}! Token: 3f02d878"

class Counter:
    """A simple counter class that keeps track of a count. Token: 3f02d878"""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the count by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count

