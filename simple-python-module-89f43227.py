"""A simple Python module with one function and one class, including a specific token in the docstring. | token=89f43227"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token '89f43227' as a constant."""
    TOKEN = '89f43227'

    def get_token(self):
        """Return the special token."""
        return self.TOKEN
