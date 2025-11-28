"""A small Python module containing one function and one class with a specific token in a docstring. | token=7251954d"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: 7251954d"""
    def __init__(self):
        self.token = "7251954d"
    
    def get_token(self):
        """Return the stored token."""
        return self.token
