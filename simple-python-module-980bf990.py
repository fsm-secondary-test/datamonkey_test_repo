"""This module contains one simple function and one simple class. The token '980bf990' is included in a class docstring. | token=980bf990"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """A simple class that holds the token '980bf990'."""
    def __init__(self):
        self.token = '980bf990'
    
    def get_token(self):
        """Return the stored token."""
        return self.token
