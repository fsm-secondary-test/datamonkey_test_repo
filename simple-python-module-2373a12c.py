"""A Python module with one function and one class, including a specific token in a docstring. | token=2373a12c"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 2373a12c"""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the count by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
