"""A Python module containing one simple function and one simple class with the token 'a9475dff' in a docstring. | token=a9475dff"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class containing the special token a9475dff as a class attribute."""

    token = 'a9475dff'

    def get_token(self):
        """Return the stored token."""
        return self.token
