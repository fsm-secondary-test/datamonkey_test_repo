"""A Python module containing a simple function and a simple class with the token '127f1e19' in the docstring. | token=127f1e19"""

def greet(name: str) -> str:
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 127f1e19."""
    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        """Increment the counter by one."""
        self.count += 1

    def reset(self) -> None:
        """Reset the counter to zero."""
        self.count = 0
