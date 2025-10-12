"""A small Python module containing one function and one class with a specific token in the docstring. | token=bdc36746"""

def greet(name):
    """Return a greeting message including the token bdc36746."""
    return f"Hello, {name}! This message includes token bdc36746."

class Counter:
    """Simple counter class with token bdc36746 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
