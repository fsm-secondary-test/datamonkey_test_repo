"""A small Python module containing one simple function and one simple class. The literal token '819cb834' is included in a docstring. | token=819cb834"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds the literal token '819cb834' as a class attribute."""
    TOKEN = '819cb834'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
