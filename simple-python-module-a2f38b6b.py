"""A small Python module with one function and one class, including a unique token in the docstring. | token=a2f38b6b"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token string 'a2f38b6b'."""

    def __init__(self):
        self.token = 'a2f38b6b'

    def get_token(self):
        """Return the stored token."""
        return self.token
