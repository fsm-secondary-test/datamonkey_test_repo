"""A small Python module with one function and one class, including a specific token in the docstring. | token=54048ab2"""

def greet(name):
    """Return a greeting message with the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 54048ab2"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
