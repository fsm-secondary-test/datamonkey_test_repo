"""This module contains one simple function and one simple class. It includes the literal token 'bbb9ab9d' in the docstring of the class. | token=bbb9ab9d"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """A simple class that holds the token 'bbb9ab9d'."""
    def __init__(self):
        self.token = 'bbb9ab9d'
    
    def get_token(self):
        """Return the stored token."""
        return self.token
