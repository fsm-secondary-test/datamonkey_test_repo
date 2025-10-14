"""A small Python module containing one function and one class with a specific token in the docstring. | token=c3b52cff"""

def greet(name):
    """Return a greeting message including the given name and token c3b52cff."""
    return f"Hello, {name}! Welcome to the c3b52cff module."

class Counter:
    """A simple counter class that increments a count. Token: c3b52cff"""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
