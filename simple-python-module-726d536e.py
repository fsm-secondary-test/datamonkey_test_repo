"""A small Python module containing one simple function and one simple class. Includes a specific token in the docstring. | token=726d536e"""

def greet(name):
    """Return a greeting message including the name and token 726d536e."""
    return f"Hello, {name}! Token: 726d536e"

class Counter:
    """Simple counter class that keeps track of a count. Token: 726d536e"""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
