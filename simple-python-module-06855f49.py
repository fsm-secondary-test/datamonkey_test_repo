"""A Python module with one function and one class, including a specific token in a docstring. | token=06855f49"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a specific token as a constant."""
    TOKEN = "06855f49"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
