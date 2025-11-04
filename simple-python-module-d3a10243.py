"""A small Python module with one function and one class including a specific token in the docstring. | token=d3a10243"""

def greet(name):
    """Return a greeting message with the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds the token d3a10243 as a string constant."""

    TOKEN = "d3a10243"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
