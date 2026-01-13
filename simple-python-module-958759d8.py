"""A Python module with one simple function and one simple class, including a literal token in a docstring. | token=958759d8"""

def greet(name):
    """Return a greeting message including the token 958759d8."""
    return f"Hello, {name}! Your token is 958759d8."

class Counter:
    """Simple counter class that uses token 958759d8 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
