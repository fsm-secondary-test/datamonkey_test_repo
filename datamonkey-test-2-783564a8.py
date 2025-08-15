"""Datamonkey Test File 2

A Python file for testing GitHub sync with code content.
"""

def datamonkey_test_function_2():
    """Test function for datamonkey verification."""
    return f"Hello from Datamonkey Test File 2!"


class DatamonkeyTestClass2:
    """Test class for datamonkey verification."""
    
    def __init__(self):
        self.name = f"Datamonkey Test Class 2"
        self.purpose = "Testing GitHub sync functionality"
        self.file_type = "python"
        self.random_suffix = "783564a8"
        self.timestamp = "1755256924"
    
    def get_info(self):
        """Get test class information."""
        return f"{self.name}: {self.purpose}"


if __name__ == "__main__":
    print(datamonkey_test_function_2())
    test_obj = DatamonkeyTestClass2()
    print(test_obj.get_info())
