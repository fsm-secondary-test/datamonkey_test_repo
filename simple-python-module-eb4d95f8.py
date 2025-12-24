"""A small Python module with one function and one class, including a specific token in a docstring. | token=eb4d95f8"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: eb4d95f8"""

    def __init__(self):
        self.token = "eb4d95f8"

    def get_token(self):
        """Return the stored token."""
        return self.token
