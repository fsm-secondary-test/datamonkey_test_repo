"""A small Python module containing one simple function and one simple class. Includes the literal token '18800c80' in a docstring. | token=18800c80"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class.

    Token: 18800c80
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
