"""A small Python module containing one function and one class. Includes the literal token 'ab7e4b4f' in a docstring. | token=ab7e4b4f"""

def greet(name):
    """Return a greeting message including the token ab7e4b4f."""
    return f"Hello, {name}! Token: ab7e4b4f"

class Counter:
    """A simple counter class with token ab7e4b4f in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
