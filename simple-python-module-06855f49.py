"""A small Python module containing one simple function and one simple class, including a specific token in a docstring. | token=06855f49"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token.

    Token: 06855f49
    """
    def __init__(self):
        self.token = "06855f49"

    def get_token(self):
        """Return the stored token."""
        return self.token
