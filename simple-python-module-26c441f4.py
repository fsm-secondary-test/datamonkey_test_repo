"""A small Python module with one function and one class, including a specific token in the docstring. | token=26c441f4"""

def greet(name):
    """Return a greeting message including the token 26c441f4."""
    return f"Hello, {name}! This is token 26c441f4."

class Counter:
    """Simple counter class with token 26c441f4 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
