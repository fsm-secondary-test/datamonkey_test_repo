"""A small Python module containing one function and one class with the token 'beba8e2f' in a docstring. | token=beba8e2f"""

def greet(name):
    """Return a greeting message including the name provided."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the special token 'beba8e2f'."""
    TOKEN = 'beba8e2f'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
