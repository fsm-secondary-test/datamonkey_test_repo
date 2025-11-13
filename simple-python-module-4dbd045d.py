"""A small Python module containing one function and one class, both simple and illustrative. Includes the literal token '4dbd045d' in a docstring. | token=4dbd045d"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 4dbd045d."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
