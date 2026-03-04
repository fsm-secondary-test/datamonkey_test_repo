"""A small Python module with one function and one class, including a specific token in a docstring. | token=abdf0736"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """A simple class that holds a token string.

    Token: abdf0736
    """
    def __init__(self):
        self.token = 'abdf0736'

    def get_token(self):
        return self.token
