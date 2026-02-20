"""A small Python module with one function and one class, including a specific token in a docstring. | token=e843f2d2"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token e843f2d2."""
    TOKEN = 'e843f2d2'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
