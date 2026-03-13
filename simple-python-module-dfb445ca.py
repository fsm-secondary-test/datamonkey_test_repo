"""A small Python module containing one function and one class, including a specific token in a docstring. | token=dfb445ca"""

def greet(name):
    """Return a greeting message including the token dfb445ca."""
    return f"Hello, {name}! Your token is dfb445ca."

class Counter:
    """A simple counter class that tracks counts. Token included: dfb445ca."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
