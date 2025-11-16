"""A small Python module with one function and one class, including a specific token in a docstring. | token=283fe99f"""

def greet(name):
    """Return a greeting message including the token 283fe99f."""
    return f"Hello, {name}! Token: 283fe99f"

class Counter:
    """A simple counter class that counts up from zero. Token: 283fe99f."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
