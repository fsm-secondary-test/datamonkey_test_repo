"""A small Python module with one function and one class, including the token '99d1cee8'. | token=99d1cee8"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token.

    Token: 99d1cee8
    """
    def __init__(self):
        self.token = '99d1cee8'

    def get_token(self):
        """Return the stored token."""
        return self.token
