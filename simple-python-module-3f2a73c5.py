"""A small Python module containing one simple function and one simple class with a specific token in a docstring. | token=3f2a73c5"""

def greet(name):
    """Return a greeting message including the given name and token 3f2a73c5."""
    return f"Hello, {name}! Token: 3f2a73c5"

class Counter:
    """A simple counter class that uses the token 3f2a73c5 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count

