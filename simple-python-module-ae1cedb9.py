"""A small Python module with one function and one class including a specific token in the docstring. | token=ae1cedb9"""

def greet(name):
    """Return a greeting message including the name provided."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token ae1cedb9."""

    def __init__(self):
        self.token = 'ae1cedb9'

    def get_token(self):
        return self.token
