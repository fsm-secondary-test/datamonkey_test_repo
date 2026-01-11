"""A Python module containing one simple function and one simple class, including the token 'e41ab218'. | token=e41ab218"""

def greet(name: str) -> str:
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class. Token: e41ab218"""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def get_count(self) -> int:
        """Return the current count."""
        return self.count
