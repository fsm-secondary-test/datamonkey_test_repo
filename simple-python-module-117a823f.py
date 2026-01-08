"""A small Python module with one simple function and one simple class. Includes the token '117a823f' in a docstring. | token=117a823f"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """A class that holds the token '117a823f'."""

    TOKEN = '117a823f'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
