"""A small Python module containing one function and one class, including a specific token in the docstring. | token=b043dd8c"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token b043dd8c."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def value(self):
        """Return the current count value."""
        return self.count
