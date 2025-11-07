"""A small Python module with one function and one class, including a literal token in a docstring. | token=c9d43748"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a constant token value 'c9d43748'."""
    TOKEN = 'c9d43748'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
