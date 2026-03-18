"""A small Python module with one function and one class, including a specific token in the docstring. | token=6c10b27c"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: 6c10b27c"""
    def __init__(self):
        self.token = "6c10b27c"
    
    def get_token(self):
        """Return the stored token."""
        return self.token
