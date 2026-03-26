"""A module with one simple function and one simple class including a specific token in a docstring. | token=e427bd00"""

def greet(name):
    """Return a greeting message including token e427bd00."""
    return f"Hello, {name}! Welcome to the e427bd00 module."

class Counter:
    """A simple counter class that uses token e427bd00 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
