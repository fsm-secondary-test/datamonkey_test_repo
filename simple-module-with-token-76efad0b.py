"""A Python module containing one function and one class, including a specific token in a docstring. | token=76efad0b"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: 76efad0b."""
    TOKEN = "76efad0b"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
