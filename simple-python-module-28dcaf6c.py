"""A small Python module containing one function and one class, including a specific token in a docstring. | token=28dcaf6c"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a specific token: 28dcaf6c"""
    TOKEN = "28dcaf6c"

    def get_token(self):
        return self.TOKEN
