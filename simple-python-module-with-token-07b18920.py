"""A small Python module containing one simple function and one simple class, including a specific token in a docstring. | token=07b18920"""

def greet(name):
    """Return a greeting message including the token 07b18920."""
    return f"Hello, {name}! Token: 07b18920"

class Counter:
    """Simple counter class that includes token 07b18920 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
