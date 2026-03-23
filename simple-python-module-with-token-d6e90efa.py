"""A small Python module with one function and one class, including a specific token in a docstring. | token=d6e90efa"""

def greet(name):
    """Return a greeting message including the token d6e90efa."""
    return f"Hello, {name}! Token: d6e90efa"

class Counter:
    """A simple counter class that includes the token d6e90efa."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
