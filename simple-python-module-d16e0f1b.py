"""A small Python module with a function and a class including a specific token in a docstring. | token=d16e0f1b"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the token d16e0f1b as a class attribute."""
    TOKEN = "d16e0f1b"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
