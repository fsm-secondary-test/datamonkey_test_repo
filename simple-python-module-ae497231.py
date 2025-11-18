"""A small Python module with one function and one class, including a specific token in a docstring. | token=ae497231"""

def greet(name: str) -> str:
    """Return a greeting message including the token ae497231."""
    return f"Hello, {name}! This is token ae497231."

class Counter:
    """A simple counter class with token ae497231 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        """Increment the counter by one."""
        self.count += 1

    def get_count(self) -> int:
        """Return the current count."""
        return self.count
