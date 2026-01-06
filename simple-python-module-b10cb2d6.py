"""A small Python module with one function and one class, including a specific token in the docstring. | token=b10cb2d6"""

def greet(name):
    """Return a greeting message including the token b10cb2d6."""
    return f"Hello, {name}! This message includes token b10cb2d6."

class Counter:
    """A simple counter class that uses token b10cb2d6 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
