"""A small Python module containing one function and one class, including a specific token in a docstring. | token=fba16769"""

def greet(name: str) -> str:
    """Return a greeting message including the token fba16769."""
    return f"Hello, {name}! This message contains token fba16769."

class SimpleCounter:
    """A simple counter class that includes the token fba16769 in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self) -> int:
        """Increment the counter by one and return the new count."""
        self.count += 1
        return self.count
    
    def reset(self) -> None:
        """Reset the counter to zero."""
        self.count = 0
