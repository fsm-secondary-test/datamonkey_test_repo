"""A small Python module containing one function and one class, including a specific token in the docstring. | token=a40bf0b8"""

def greet(name):
    """Return a greeting message including the token a40bf0b8."""
    return f"Hello, {name}! This is token a40bf0b8."

class Counter:
    """A simple counter class that includes token a40bf0b8 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
