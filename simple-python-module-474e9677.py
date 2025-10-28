"""A small Python module including a simple function and a simple class. The module contains the literal token '474e9677' in a docstring. | token=474e9677"""

def greet(name):
    """Return a greeting message including the name and the token '474e9677'."""
    return f"Hello, {name}! Token: 474e9677"

class Counter:
    """A simple counter class that tracks counts and includes the token '474e9677' in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self):
        """Get the current count."""
        return self.count
