"""This module contains a simple function and a simple class, including the literal token 'a78761fd' in a docstring. | token=a78761fd"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds the token 'a78761fd' as a class attribute."""
    TOKEN = 'a78761fd'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
