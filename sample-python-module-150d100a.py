"""A small Python module with one simple function and one simple class, including the literal token '150d100a' in a docstring. | token=150d100a"""

def greet(name):
    """Return a greeting message including the user's name."""
    return f"Hello, {name}! Welcome to the 150d100a example module."

class Counter:
    """A simple counter class that counts up from zero. Token included: 150d100a"""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
