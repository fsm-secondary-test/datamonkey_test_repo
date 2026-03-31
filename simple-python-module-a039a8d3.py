"""A small Python module containing one function and one class, including a specific token in a docstring. | token=a039a8d3"""

def greet(name):
    """Return a greeting message including the token a039a8d3."""
    return f"Hello, {name}! Token: a039a8d3"

class Counter:
    """A simple counter class that counts up from zero. Token: a039a8d3"""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
