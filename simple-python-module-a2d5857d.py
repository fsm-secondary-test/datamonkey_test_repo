"""A module containing one simple function and one simple class, including a specific token in a docstring. | token=a2d5857d"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class that increments count. Token: a2d5857d"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
