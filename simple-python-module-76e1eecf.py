"""A small Python module with one simple function and one simple class, including the token '76e1eecf' in a docstring. | token=76e1eecf"""

def greet(name):
    """Return a greeting message for the given name. Token: 76e1eecf."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class that counts up from zero. Token: 76e1eecf."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
