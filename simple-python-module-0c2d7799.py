"""A small Python module containing one function and one class with a special token in the docstring. | token=0c2d7799"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class including token 0c2d7799 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
