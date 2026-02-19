"""A small Python module containing one function and one class. Includes a literal token 'a9238988' in a docstring. | token=a9238988"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token string 'a9238988'."""
    TOKEN = 'a9238988'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
