# Test Project - Simple Test Script
print("Welcome to Test Project!")
print("This is a simple test to verify the setup works.")

def test_function():
    """A simple test function"""
    result = 2 + 2
    assert result == 4, "Math is broken!"
    return result

if __name__ == "__main__":
    test_result = test_function()
    print(f"Test passed! Result: {test_result}")
