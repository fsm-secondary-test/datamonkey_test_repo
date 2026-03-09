"""A small Python module containing one simple function and one simple class, including the literal token '08a3e899' in a docstring. | token=08a3e899"""

def greet(name):
    """Return a greeting message with the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token value '08a3e899'."""

    def __init__(self):
        self.token = '08a3e899'

    def get_token(self):
        """Return the stored token."""
        return self.token
