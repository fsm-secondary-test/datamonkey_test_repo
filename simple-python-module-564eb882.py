"""A simple Python module with one function and one class. Includes a literal token in a docstring. | token=564eb882"""

def greet(name):
    """Return a greeting message including the token 564eb882."""
    return f"Hello, {name}! Token: 564eb882"

class Counter:
    """A simple counter class with token 564eb882 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
