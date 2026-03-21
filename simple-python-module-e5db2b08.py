"""A small Python module with one function and one class, including a specific token in the docstring. | token=e5db2b08"""

def greet(name):
    """Return a greeting message including the user's name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a specific token string.

    Token: e5db2b08
    """
    def __init__(self):
        self.token = "e5db2b08"

    def get_token(self):
        """Return the stored token."""
        return self.token
