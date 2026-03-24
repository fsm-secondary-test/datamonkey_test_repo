"""A small Python module with one function and one class, including a specific token in a docstring. | token=022e14dc"""

def greet(name):
    """Return a greeting message including the token 022e14dc."""
    return f"Hello, {name}! Token: 022e14dc"

class Counter:
    """A simple counter class that includes the token 022e14dc in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1
        return self.count

    def reset(self):
        """Reset the counter to 0."""
        self.count = 0
