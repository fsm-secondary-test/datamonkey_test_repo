"""A small Python module with one function and one class, including a literal token in a docstring. | token=f0d811e4"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token 'f0d811e4' as a class attribute."""
    token = 'f0d811e4'

    def get_token(self):
        """Return the token."""
        return self.token
