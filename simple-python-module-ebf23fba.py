"""A small Python module with one function and one class including a specific token in the docstring. | token=ebf23fba"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """SimpleCounter class tracks a count. Token: ebf23fba"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
