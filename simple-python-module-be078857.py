"""A small Python module containing one function and one class, including a token in a docstring. | token=be078857"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a specific token: be078857."""

    def __init__(self):
        self.token = "be078857"

    def get_token(self):
        """Return the stored token."""
        return self.token
