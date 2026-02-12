"""A small Python module containing one function and one class, including a specific token in a docstring. | token=29fc422c"""

def greet(name):
    """Return a greeting message including the token 29fc422c."""
    return f"Hello, {name}! Token: 29fc422c"

class Counter:
    """Simple counter class with token 29fc422c in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
