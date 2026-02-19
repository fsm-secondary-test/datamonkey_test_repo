"""A small Python module with one function and one class, including a specific token in a docstring. | token=833ccf08"""

def greet(name):
    """Return a greeting message including the token 833ccf08."""
    return f"Hello, {name}! Token: 833ccf08"

class Counter:
    """A simple counter class.
    Token included: 833ccf08
    """

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
