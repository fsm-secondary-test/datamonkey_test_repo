"""A small Python module with one function and one class, including a specific token. | token=78a94a76"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token."""
    TOKEN = '78a94a76'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
