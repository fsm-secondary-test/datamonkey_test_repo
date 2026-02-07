"""A small Python module with one function and one class. Includes the token '3a9fe383' in a docstring. | token=3a9fe383"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class that includes token '3a9fe383' in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
