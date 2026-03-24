"""This Python module includes a simple function and a simple class, both demonstrating basic usage. The module contains the token '8f666048' in a constant string. | token=8f666048"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token string constant."""

    TOKEN = "8f666048"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
