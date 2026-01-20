"""A small Python module containing one function and one class, including a specific token in a docstring. | token=4226b023"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class to hold a special token string: '4226b023'."""

    def __init__(self):
        self.token = '4226b023'

    def get_token(self):
        """Return the stored token."""
        return self.token
