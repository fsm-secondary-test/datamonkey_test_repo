"""A small Python module with one function and one class, including a specific token in a docstring. | token=8cdbc7d4"""

def greet(name):
    """Return a greeting message for the given name. Token: 8cdbc7d4"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token inside docstring: 8cdbc7d4"""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the count by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
