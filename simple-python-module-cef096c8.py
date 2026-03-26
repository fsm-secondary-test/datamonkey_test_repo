"""A small Python module with one simple function and one simple class, including the token 'cef096c8' in a docstring. | token=cef096c8"""

def greet(name):
    """Return a greeting message including the token cef096c8."""
    return f"Hello, {name}! Token: cef096c8"

class Counter:
    """Simple counter class with token cef096c8 in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self):
        """Get the current count."""
        return self.count
