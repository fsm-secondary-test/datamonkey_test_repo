"""This module contains a simple function and a simple class, including the literal token 'e0034863' in a docstring. | token=e0034863"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the special token e0034863."""
    token = 'e0034863'

    def get_token(self):
        """Return the stored token."""
        return self.token
