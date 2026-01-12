"""A small Python module containing one function and one class with the token '07137cac' included in a docstring. | token=07137cac"""

def greet(name: str) -> str:
    """Return a greeting message for the given name. Token: 07137cac"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 07137cac"""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self) -> int:
        """Get the current count."""
        return self.count
