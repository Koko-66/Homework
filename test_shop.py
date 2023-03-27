
"""Unittests"""
import unittest
from shop import(setup,
    validate_if_in_range,
    validate_if_number,
    validate_confirmation,
    validate_budget)


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

    def test_validate_if_number(self):
        """Test number validation when input is not a number"""
        user_input = "l"
        with self.assertRaises(ValueError):
            validate_if_number(user_input)
    
    def test_validate_if_negative_number(self):
        """Test number validation when input is negative"""    
        user_input = "-2"
        with self.assertRaises(ValueError):
            validate_if_number(user_input)

    def test_validate_confirmation(self):
        """Test confirmation input if not y or n"""
        user_input = 0
        with self.assertRaises(ValueError):
            validate_confirmation(user_input)

    def test_validate_confirmation_if_no(self):
        """Test if program exits if input == n"""
        user_input = "n"
        with self.assertRaises(SystemExit) as error:
            validate_confirmation(user_input)
            self.assertEqual(error.exception.code, 1)

    def validate_budget(self):
        """Test if budget is lower than item price"""
        budget = 10
        item_price = 20
        with self.assertRaises(ValueError):
            validate_budget(budget, item_price)

    
if __name__ == '__main__':
    unittest.main()
