"""A Python module containing one simple function and one simple class, including the token '90f23e69' in a docstring. | token=90f23e69"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token: 90f23e69."""
    def __init__(self):
        self.token = '90f23e69'
    
    def get_token(self):
        """Return the stored token."""
        return self.token
