
"""Unittests"""
import unittest
from shop import setup, validate_if_in_range


class TestShop(unittest.TestCase):
    """Test case for shop functions"""

    stock = {'charger': 11, 'kettle': 25,
         'headphones': 75, 'stereo': 140, 'Robot': 99.50}

    def test_setup(self):
        """Test setup function"""
        self.assertEqual(setup(self.stock)[0], {"charger": 11})

    def test_validate_if_in_range(self):
        """Test range validation"""
        user_input = 9
        with self.assertRaises(ValueError):
            validate_if_in_range(user_input, self.stock)
            


if __name__ == '__main__':
    unittest.main()