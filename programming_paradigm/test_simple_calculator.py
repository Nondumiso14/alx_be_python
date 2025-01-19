class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(7, 4), 3)
        self.assertEqual(self.calc.subtract(4, -3), 7)

    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(4, 10), 40)
        self.assertEqual(self.calc.multiply(5, -4), -20)

    def test_division(self):
        """Test the division method and handle exception raises"""
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(-12, 8), -1.5)
        self.assertIsNone(self.calc.divide(9, 0))
