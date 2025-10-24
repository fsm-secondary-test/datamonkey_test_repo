"""A small Python module containing one function and one class. Includes the literal token '59e11262' in the docstring. | token=59e11262"""

def greet(name):
    """Return a greeting message including the provided name. Token: 59e11262"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 59e11262"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
