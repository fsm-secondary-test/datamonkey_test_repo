"""A simple Python module with one function and one class, including a specific token in the docstring. | token=0032d62b"""

def greet(name):
    """Return a greeting message for the given name. Token: 0032d62b"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 0032d62b"""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count."""
        return self.count
