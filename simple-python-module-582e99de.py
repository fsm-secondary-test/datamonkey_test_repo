"""A small Python module with one function and one class, including the token '582e99de' in a string constant. | token=582e99de"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """A simple class holding a constant token."""
    TOKEN = '582e99de'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
