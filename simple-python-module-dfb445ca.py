"""A small Python module containing one simple function and one simple class. Includes the token 'dfb445ca' in a docstring. | token=dfb445ca"""

def greet(name):
    """Return a greeting message including the provided name.
    Token included: dfb445ca"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class that increments a count.
    Token included: dfb445ca"""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
