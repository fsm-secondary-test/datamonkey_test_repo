"""A small Python module with one function and one class, including a literal token in a docstring. | token=ca592a3b"""

def greet(name):
    """Return a greeting message including the token ca592a3b."""
    return f"Hello, {name}! Token: ca592a3b"

class Counter:
    """A simple counter class that includes token ca592a3b in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self):
        """Get the current count."""
        return self.count
