"""A small Python module containing one function and one class, including a specific token in the docstring. | token=8eb984cc"""

def greet(name: str) -> str:
    """Return a greeting message including the given name. Token: 8eb984cc"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 8eb984cc"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self) -> int:
        return self.count
