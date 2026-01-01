"""A small Python module with one function and one class, including a specific token in a docstring. | token=a5edd0a9"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token string 'a5edd0a9'."""

    def __init__(self):
        self.token = 'a5edd0a9'

    def get_token(self):
        """Return the stored token."""
        return self.token
