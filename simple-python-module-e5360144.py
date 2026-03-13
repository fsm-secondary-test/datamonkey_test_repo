"""A small Python module with one simple function and one simple class, including the token 'e5360144' in a string constant. | token=e5360144"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token."""
    TOKEN = "e5360144"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
