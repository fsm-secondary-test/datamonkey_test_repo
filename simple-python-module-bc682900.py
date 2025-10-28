"""A small Python module containing one function and one class, including a special token in a docstring. | token=bc682900"""

def greet(name):
    """Return a greeting message including the given name and token bc682900."""
    return f"Hello, {name}! This is token bc682900."

class Counter:
    """A simple counter class that counts up from zero. Token: bc682900."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
