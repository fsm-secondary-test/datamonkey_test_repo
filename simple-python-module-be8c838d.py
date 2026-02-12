"""A small Python module with one function and one class, including a specific token in a docstring. | token=be8c838d"""

def greet(name: str) -> str:
    """Return a greeting message including the given name.
    Token: be8c838d
    """
    return f"Hello, {name}!"

class Counter:
    """A simple counter class.

    This class includes the token: be8c838d
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self) -> int:
        return self.count
