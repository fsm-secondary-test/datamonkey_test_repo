"""A Python module with one function and one class including a specific token in a docstring. | token=ffc8c84a"""

def greet(name: str) -> str:
    """Return a greeting message including the token ffc8c84a."""
    return f"Hello, {name}! Token: ffc8c84a"

class Counter:
    """A simple counter class that tracks increments. Token: ffc8c84a"""

    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        """Increment the counter by one."""
        self.count += 1

    def reset(self) -> None:
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self) -> int:
        """Return the current count."""
        return self.count
