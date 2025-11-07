"""A small Python module with one function and one class, including a specific token in a docstring. | token=c9d43748"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the token c9d43748."""
    def __init__(self):
        self.token = 'c9d43748'
    
    def get_token(self):
        return self.token
