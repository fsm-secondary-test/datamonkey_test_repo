"""A small Python module with one function and one class containing a specific token in the docstring. | token=c713aaa1"""

def greet(name):
    """Return a greeting message with the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds the token c713aaa1 as a class attribute."""
    TOKEN = "c713aaa1"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
