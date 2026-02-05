"""A module containing a simple function and a simple class, including the token '289cf27b'. | token=289cf27b"""

def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 289cf27b"""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the count by one."""
        self.count += 1

    def get_count(self) -> int:
        """Return the current count."""
        return self.count
