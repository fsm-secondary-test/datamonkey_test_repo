"""A small Python module containing one simple function and one simple class, including the token '87224852' in a docstring. | token=87224852"""

def greet(name):
    """Return a greeting message including the name provided."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the special token '87224852' as a class attribute."""
    token = '87224852'

    def get_token(self):
        """Return the stored token."""
        return self.token
