"""A small Python module containing one function and one class, including a literal token in a docstring. | token=7ed6454f"""

def greet(name):
    """Return a greeting message including the token 7ed6454f."""
    return f"Hello, {name}! Token: 7ed6454f"

class Counter:
    """A simple counter class that counts up from zero. Token: 7ed6454f included in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
