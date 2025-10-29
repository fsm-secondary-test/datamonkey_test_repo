"""A small Python module containing a simple function and a simple class. Includes the token 'aa7f0013' in a docstring. | token=aa7f0013"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: aa7f0013."""
    def __init__(self):
        self.token = 'aa7f0013'
    
    def get_token(self):
        """Return the stored token."""
        return self.token
