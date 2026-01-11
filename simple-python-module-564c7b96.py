"""A small Python module with one function and one class including a specific token in a docstring. | token=564c7b96"""

def greet(name):
    """Return a greeting message including the token 564c7b96."""
    return f"Hello, {name}! Token: 564c7b96"

class Counter:
    """A simple counter class that includes the token 564c7b96."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
