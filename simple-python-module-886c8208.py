"""A small Python module containing one function and one class with the token '886c8208' in a docstring. | token=886c8208"""

def greet(name):
    """Return a greeting message that includes the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a token string.

    Token: 886c8208
    """
    def __init__(self, token='886c8208'):
        self.token = token

    def get_token(self):
        """Return the stored token."""
        return self.token
