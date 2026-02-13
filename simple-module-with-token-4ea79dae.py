"""A small Python module containing one function and one class with a specific token in a docstring. | token=4ea79dae"""

def greet(name: str) -> str:
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 4ea79dae"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
