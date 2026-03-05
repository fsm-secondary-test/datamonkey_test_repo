"""A small Python module containing one function and one class, including the token '08aaad24' in a docstring. | token=08aaad24"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token '08aaad24'."""

    def __init__(self):
        self.token = '08aaad24'

    def get_token(self):
        """Return the stored token."""
        return self.token
