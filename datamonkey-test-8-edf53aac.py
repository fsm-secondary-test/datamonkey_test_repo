"""Datamonkey Test File 8

A Python file for testing GitHub sync with code content.
"""

def datamonkey_test_function_8():
    """Test function for datamonkey verification."""
    return f"Hello from Datamonkey Test File 8!"


class DatamonkeyTestClass8:
    """Test class for datamonkey verification."""
    
    def __init__(self):
        self.name = f"Datamonkey Test Class 8"
        self.purpose = "Testing GitHub sync functionality"
        self.file_type = "python"
        self.random_suffix = "edf53aac"
        self.timestamp = "1755205181"
    
    def get_info(self):
        """Get test class information."""
        return f"{self.name}: {self.purpose}"


if __name__ == "__main__":
    print(datamonkey_test_function_8())
    test_obj = DatamonkeyTestClass8()
    print(test_obj.get_info())
