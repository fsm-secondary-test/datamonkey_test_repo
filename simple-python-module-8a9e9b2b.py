"""A small Python module with one function and one class, including a specific token in the docstring. | token=8a9e9b2b"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the token '8a9e9b2b' as a class attribute."""
    token = '8a9e9b2b'

    def get_token(self):
        """Return the stored token."""
        return self.token
