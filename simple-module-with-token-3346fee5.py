"""A small Python module containing one function and one class, including the token '3346fee5' in a docstring. | token=3346fee5"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: 3346fee5"""
    TOKEN = "3346fee5"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
