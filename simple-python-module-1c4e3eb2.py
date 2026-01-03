"""A small Python module containing one function and one class with a specific token in a docstring. | token=1c4e3eb2"""

def greet(name: str) -> str:
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 1c4e3eb2 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self) -> int:
        """Increment the counter by one and return the new value."""
        self.count += 1
        return self.count
