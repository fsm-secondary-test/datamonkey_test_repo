"""A Python module containing one simple function and one simple class, including a specific token in a docstring. | token=c727a940"""

def greet(name):
    """Return a greeting message including the token c727a940."""
    return f"Hello, {name}! Token: c727a940"

class Counter:
    """A simple counter class including the token c727a940."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def __str__(self):
        return f"Counter value: {self.count} (token c727a940)"
