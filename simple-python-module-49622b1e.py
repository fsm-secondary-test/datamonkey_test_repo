"""A small Python module with one function and one class. Includes the token '49622b1e' in a docstring. | token=49622b1e"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds the token '49622b1e' as a constant."""
    TOKEN = '49622b1e'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
