"""A small Python module with one function and one class, including a specific token in the docstring. | token=9575f521"""

def greet(name):
    """Return a greeting message including the token 9575f521."""
    return f"Hello, {name}! Token: 9575f521"

class Counter:
    """A simple counter class that stores count. Token: 9575f521."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the count by one."""
        self.count += 1

    def reset(self):
        """Reset the count to zero."""
        self.count = 0

    def get_count(self):
        """Return the current count."""
        return self.count
