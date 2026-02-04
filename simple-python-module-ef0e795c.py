"""A module containing one simple function and one simple class with a specific token in a docstring. | token=ef0e795c"""

def greet(name: str) -> str:
    """Return a greeting message including the token ef0e795c."""
    return f"Hello, {name}! Your token is ef0e795c."

class Counter:
    """A simple counter class with token ef0e795c in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        """Increment the counter by 1."""
        self.count += 1

    def get_count(self) -> int:
        """Return the current count."""
        return self.count
