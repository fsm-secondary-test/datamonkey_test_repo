"""A small Python module with one function and one class, including a specific token in a docstring. | token=0531ef7c"""

def greet(name):
    """Return a greeting message including the token 0531ef7c."""
    return f"Hello, {name}! Your token is 0531ef7c."

class SimpleCounter:
    """A simple counter class that includes the token 0531ef7c in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self):
        """Return the current count."""
        return self.count
