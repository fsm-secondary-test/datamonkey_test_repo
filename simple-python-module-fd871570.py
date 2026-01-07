"""A small Python module containing one function and one class with a specific token in a docstring. | token=fd871570"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token string 'fd871570'."""

    def __init__(self):
        self.token = 'fd871570'

    def get_token(self):
        """Return the stored token."""
        return self.token
