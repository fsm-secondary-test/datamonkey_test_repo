"""A Python module containing one simple function and one simple class with a specific token in a docstring. | token=92ea7879"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token string '92ea7879'."""

    TOKEN = '92ea7879'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
