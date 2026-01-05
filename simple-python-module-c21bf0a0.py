"""A Python module containing one simple function and one simple class with a specific token in a docstring. | token=c21bf0a0"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a specific token: c21bf0a0."""
    
    def __init__(self):
        self.token = 'c21bf0a0'
    
    def get_token(self):
        """Return the stored token."""
        return self.token
