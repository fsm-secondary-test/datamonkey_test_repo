"""A small Python module containing one function and one class. Includes the token 'ee04bcda' in a docstring. | token=ee04bcda"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds the special token 'ee04bcda'."""
    TOKEN = 'ee04bcda'

    def get_token(self):
        """Return the token."""
        return self.TOKEN
