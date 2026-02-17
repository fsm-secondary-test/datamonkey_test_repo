"""A basic Python module containing one function and one class with a specific token in the docstring. | token=e2baf0bc"""

def greet(name):
    """Return a greeting message for the given name. Token: e2baf0bc"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: e2baf0bc"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
