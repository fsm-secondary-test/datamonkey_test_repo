"""A small Python module containing one function and one class, including the token 'fc374737' in a docstring. | token=fc374737"""

def greet(name: str) -> str:
    """Return a greeting message including the token 'fc374737'."""
    return f"Hello, {name}! Your token is fc374737."

class Counter:
    """A simple counter class that includes the token 'fc374737' in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        """Increment the counter by one."""
        self.count += 1

    def reset(self) -> None:
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self) -> int:
        """Get the current count."""
        return self.count
