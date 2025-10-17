"""A small Python module containing one function and one class, with a literal token included in a docstring. | token=8a9e9b2b"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token string.

    Token: 8a9e9b2b
    """
    def __init__(self):
        self.token = "8a9e9b2b"

    def get_token(self):
        """Return the stored token."""
        return self.token
