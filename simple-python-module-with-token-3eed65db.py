"""A small Python module containing one simple function and one class with a specific token in a docstring. | token=3eed65db"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token '3eed65db' in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
