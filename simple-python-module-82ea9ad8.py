"""A small Python module with one function and one class. Includes a specific token in a docstring. | token=82ea9ad8"""

def greet(name):
    """Return a greeting message including the given name.
    Token: 82ea9ad8
    """
    return f"Hello, {name}!"

class Counter:
    """Simple counter class.
    Token: 82ea9ad8
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
