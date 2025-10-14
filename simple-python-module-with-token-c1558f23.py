"""A small Python module with one function and one class, including the token 'c1558f23' in a docstring. | token=c1558f23"""

def greet(name: str) -> str:
    """Return a greeting message for the given name. Token: c1558f23"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: c1558f23"""

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
