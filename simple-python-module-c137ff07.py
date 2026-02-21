"""A small Python module with a function and a class including a specific token in the docstring. | token=c137ff07"""

def greet(name: str) -> str:
    """Return a greeting message including the token c137ff07."""
    return f"Hello, {name}! Welcome to the c137ff07 module."

class Counter:
    """Simple counter class that uses token c137ff07 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self) -> int:
        """Return the current count."""
        return self.count
