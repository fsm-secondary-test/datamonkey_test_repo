"""A Python module containing one simple function and one simple class with the token 'dea0bfef' included in a docstring. | token=dea0bfef"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token dea0bfef in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
