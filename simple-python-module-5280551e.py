"""A small Python module containing one function and one class. The module includes the token '5280551e' in the class docstring. | token=5280551e"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the token '5280551e'."""
    def __init__(self):
        self.token = '5280551e'

    def get_token(self):
        """Return the stored token."""
        return self.token
