"""A small Python module with one function and one class including a specific token in a docstring. | token=c95af520"""

def greet(name):
    """Return a simple greeting message."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the token c95af520 as a string constant."""
    TOKEN = 'c95af520'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
