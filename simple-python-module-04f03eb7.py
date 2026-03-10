"""A small Python module with one simple function and one simple class, including a specific token in a docstring. | token=04f03eb7"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """A simple class holding a token string '04f03eb7'."""

    def __init__(self):
        self.token = '04f03eb7'

    def get_token(self):
        """Return the stored token."""
        return self.token
