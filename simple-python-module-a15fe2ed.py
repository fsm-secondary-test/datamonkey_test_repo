"""A small Python module containing one function and one class, including a specific token in a docstring. | token=a15fe2ed"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: a15fe2ed"""
    def __init__(self):
        self.token = 'a15fe2ed'
    
    def get_token(self):
        """Return the stored token."""
        return self.token
