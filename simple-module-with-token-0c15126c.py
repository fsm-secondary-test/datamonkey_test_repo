"""A small Python module with one function and one class, including a specific token in a docstring. | token=0c15126c"""

def greet(name):
    """Return a greeting message including the token 0c15126c."""
    return f"Hello, {name}! Token: 0c15126c"

class Counter:
    """Simple counter class that demonstrates usage with token 0c15126c."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
