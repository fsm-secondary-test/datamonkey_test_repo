"""A small Python module including one function and one class, with a specific token in the docstring. | token=3f02d878"""

def greet(name):
    """Return a greeting message including the token 3f02d878."""
    return f"Hello, {name}! Token: 3f02d878"

class Counter:
    """A simple counter class that includes token 3f02d878 in the docstring."""
    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
