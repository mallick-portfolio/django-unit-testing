from django.test import SimpleTestCase
from app.calc import subtract, add

"""Test subtract function"""

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_subtract_two_positive(self):
        """Test subtracting two positive numbers"""
        result = subtract(4, 2)
        self.assertEqual(result, 2)
    
    def test_subtract_two_negative(self):
        """Test subtracting two negative numbers"""
        result = subtract(-4, -2)
        self.assertEqual(result, -2)
    
    def test_add_two_positive(self):
        """Test adding two positive numbers"""
        result = add(4, 2)
        self.assertEqual(result, 6)