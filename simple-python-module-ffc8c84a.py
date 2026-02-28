"""A small Python module containing one function and one class, including a literal token in a docstring. | token=ffc8c84a"""

def greet(name):
    """Return a greeting message including the token ffc8c84a."""
    return f"Hello, {name}! Token: ffc8c84a"

class SimpleCounter:
    """A simple counter class with token ffc8c84a in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
