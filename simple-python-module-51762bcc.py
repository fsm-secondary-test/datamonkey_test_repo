"""A Python module containing a simple function and a simple class, including the literal token '51762bcc' in a docstring. | token=51762bcc"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a token string '51762bcc'."""
    TOKEN = '51762bcc'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
