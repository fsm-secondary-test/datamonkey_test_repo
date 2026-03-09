"""This module contains a simple function and a simple class. The token '6c276c34' is included in the class docstring. | token=6c276c34"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """A class that holds a token string '6c276c34'."""
    def __init__(self):
        self.token = '6c276c34'

    def get_token(self):
        """Return the stored token."""
        return self.token
