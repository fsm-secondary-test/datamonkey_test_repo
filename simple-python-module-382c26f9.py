"""A Python module with one function and one class, including a literal token in a docstring. | token=382c26f9"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: '382c26f9'."""

    def __init__(self):
        self.token = '382c26f9'

    def get_token(self):
        """Return the stored token."""
        return self.token
