"""A small Python module with one simple function and one simple class, including the token '9ec82a8f' in a docstring. | token=9ec82a8f"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class.

    Token: 9ec82a8f
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
