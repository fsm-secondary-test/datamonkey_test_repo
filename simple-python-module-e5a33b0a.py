"""A small Python module with one simple function and one simple class including a literal token in docstring. | token=e5a33b0a"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token 'e5a33b0a'."""

    def __init__(self):
        self.token = 'e5a33b0a'

    def get_token(self):
        """Return the stored token."""
        return self.token
