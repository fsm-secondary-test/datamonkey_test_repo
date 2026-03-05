"""A Python module with one simple function and one simple class, including a specific token in a docstring. | token=a7cb95f0"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a token string: a7cb95f0."""
    def __init__(self):
        self.token = 'a7cb95f0'
    
    def get_token(self):
        return self.token
