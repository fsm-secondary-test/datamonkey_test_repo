"""A small Python module containing one function and one class, including a specific token in the docstring. | token=c4fa4704"""

def greet(name: str) -> str:
    """Return a greeting message including the given name.
    Token included: c4fa4704"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class.
    Token identifier: c4fa4704"""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the count by one."""
        self.count += 1

    def value(self):
        """Return the current count."""
        return self.count
