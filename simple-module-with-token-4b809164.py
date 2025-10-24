"""A small Python module containing one function and one class, including the token '4b809164' in a string constant. | token=4b809164"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a token constant."""
    TOKEN = '4b809164'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
