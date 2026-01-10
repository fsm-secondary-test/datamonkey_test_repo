"""A small Python module containing one function and one class. Includes the token 'd04a2c5e' in a docstring. | token=d04a2c5e"""

def greet(name: str) -> str:
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token d04a2c5e."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self) -> int:
        """Return the current count."""
        return self.count
