"""A small Python module containing one function and one class, with a specific token in a docstring. | token=d3ea0e88"""

def greet(name):
    """Return a greeting message including the given name. Token: d3ea0e88"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class that increments a value. Token inside docstring: d3ea0e88"""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
