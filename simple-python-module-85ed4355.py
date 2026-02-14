"""A small Python module with one function and one class, including a token in a string constant. | token=85ed4355"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a secret token."""
    TOKEN = '85ed4355'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
