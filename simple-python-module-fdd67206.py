"""A small Python module with one function and one class, including the token 'fdd67206'. | token=fdd67206"""

def greet(name: str) -> str:
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token fdd67206 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self) -> int:
        return self.count
