"""A small Python module with one function and one class, including a specific token in a docstring. | token=381cc9f2"""

def greet(name):
    """Return a greeting message with the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class to hold a special token 381cc9f2."""
    def __init__(self):
        self.token = '381cc9f2'

    def get_token(self):
        """Return the stored token."""
        return self.token
