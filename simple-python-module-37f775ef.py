"""A small Python module containing one simple function and one simple class. Includes the token '37f775ef' in a docstring. | token=37f775ef"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token '37f775ef' as a class attribute."""
    token = '37f775ef'

    def get_token(self):
        """Return the stored token."""
        return self.token
