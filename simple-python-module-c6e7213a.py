"""A Python module with one simple function and one simple class, including a specific token in a docstring. | token=c6e7213a"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token string.

    Token: c6e7213a
    """
    def __init__(self):
        self.token = "c6e7213a"

    def get_token(self):
        return self.token
