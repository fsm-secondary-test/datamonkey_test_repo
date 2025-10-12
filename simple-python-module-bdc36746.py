"""A small Python module with one function and one class, including a literal token in the docstring. | token=bdc36746"""

def greet(name: str) -> str:
    """Return a greeting message including the given name. Token: bdc36746"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: bdc36746"""
    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        """Increment the counter by 1."""
        self.count += 1

    def value(self) -> int:
        """Return the current count value."""
        return self.count
