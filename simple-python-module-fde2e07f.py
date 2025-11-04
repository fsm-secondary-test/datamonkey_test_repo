"""This module contains a simple function and a simple class, including the specified token in a docstring. | token=fde2e07f"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: fde2e07f"""

    def __init__(self):
        self.token = "fde2e07f"

    def get_token(self):
        """Return the stored token."""
        return self.token
