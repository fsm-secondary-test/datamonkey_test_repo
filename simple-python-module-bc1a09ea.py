"""A small Python module with one function and one class including a specific token in a docstring. | token=bc1a09ea"""

def greet(name):
    """Return a greeting message including token bc1a09ea."""
    return f"Hello, {name}! This message includes token bc1a09ea."

class Counter:
    """A simple counter class that includes token bc1a09ea in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
