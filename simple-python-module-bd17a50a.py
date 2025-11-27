"""A small Python module containing one function and one class, including a specific token in the docstring. | token=bd17a50a"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token."""
    TOKEN = 'bd17a50a'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
