"""A small Python module containing one simple function and one simple class with a specific token in a docstring. | token=ec152f3b"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: ec152f3b"""
    def __init__(self, token=None):
        if token is None:
            token = 'ec152f3b'
        self.token = token
    
    def get_token(self):
        """Return the stored token."""
        return self.token
