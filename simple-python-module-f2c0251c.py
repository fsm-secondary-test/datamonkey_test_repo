"""A small Python module with one function and one class including a specific token in a docstring. | token=f2c0251c"""

def greet(name):
    """Return a greeting message including the token f2c0251c."""
    return f"Hello, {name}! Welcome to the module f2c0251c."

class Counter:
    """A simple counter class that includes token f2c0251c."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
