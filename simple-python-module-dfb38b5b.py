"""A small Python module containing one function and one class, including the token 'dfb38b5b' in a docstring. | token=dfb38b5b"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token.

    Token: dfb38b5b
    """

    def __init__(self):
        self.token = 'dfb38b5b'

    def get_token(self):
        """Return the stored token."""
        return self.token
