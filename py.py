import sys
import unittest

def multiply_numbers(num1, num2):
    """
    Function to multiply two numbers.

    Parameters:
        num1 (float): First number.
        num2 (float): Second number.

    Returns:
        float: Result of multiplication.
    """
    return num1 * num2

class TestMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply_numbers(3, 4), 12)

    def test_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, -3), 6)

    def test_mixed_sign_numbers(self):
        self.assertEqual(multiply_numbers(5, -3), -15)

    def test_zero(self):
        self.assertEqual(multiply_numbers(0, 10), 0)

if __name__ == "__main__":
    # Running unit tests
    unittest.main(argv=sys.argv[:1], exit=False)
    if len(sys.argv) != 3:
        print("Usage: python program.py <number1> <number2>")
        sys.exit(1)
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please enter valid numbers.")
        sys.exit(1)
    
    result = multiply_numbers(num1, num2)
    print("Result:", result)