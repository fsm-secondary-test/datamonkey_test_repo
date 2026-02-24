"""A small Python module containing one function and one class. The literal token '39f3e792' is included in a docstring. | token=39f3e792"""

def greet(name):
    """Return a greeting message including the user's name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds the token '39f3e792' as a class attribute."""
    TOKEN = '39f3e792'

    def get_token(self):
        """Return the token."""
        return self.TOKEN
