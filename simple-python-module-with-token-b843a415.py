"""A Python module containing one simple function and one simple class, including a literal token in the code. | token=b843a415"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token."""
    TOKEN = 'b843a415'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
