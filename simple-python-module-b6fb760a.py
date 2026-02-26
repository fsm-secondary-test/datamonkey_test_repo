"""A small Python module with one function and one class, including a specific token in a docstring. | token=b6fb760a"""

def greet(name):
    """Return a greeting message including the given name and token b6fb760a."""
    return f"Hello, {name}! Token: b6fb760a"

class Counter:
    """A simple counter class with token b6fb760a in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
