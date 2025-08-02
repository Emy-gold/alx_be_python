import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Create a calculator instance before each test"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the add method"""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test mixed positive/negative
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
    
    def test_subtraction(self):
        """Test the subtract method"""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test mixed positive/negative
        self.assertEqual(self.calc.subtract(1, -1), 2)
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiplication(self):
        """Test the multiply method"""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Test mixed positive/negative
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test identity
        self.assertEqual(self.calc.multiply(1, 5), 5)
    
    def test_division(self):
        """Test the divide method"""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test fractional result
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()