
"""Unittests"""
import unittest
from unittest.mock import patch

from shop import(setup,
    validate_if_in_range,
    validate_if_number,
    validate_confirmation,
    validate_budget,
    validate_attempts,
    validate_if_not_empty,
    make_selection)


class TestShop(unittest.TestCase):
    """Test case for shop functions"""

    stock = {'charger': 11, 'kettle': 25,
         'headphones': 75, 'stereo': 140, 'Robot': 99.50}
    item_list = [{'charger': 11}, {'kettle': 25}, {
        'headphones': 75}, {'stereo': 140}, {'robot': 99.5}, 'Exit shop?']

    def test_setup(self):
        """Test setup function"""
        self.assertEqual(setup(self.stock)[0], {"charger": 11})

    def test_validate_if_in_range(self):
        """Test input validation for range"""
        user_input = 9
        with self.assertRaises(ValueError):
            validate_if_in_range(user_input, self.stock)

    def test_validate_if_number(self):
        """Test number validation when input is not a number"""
        # user_input = "l"
        with self.assertRaises(ValueError):
            validate_if_number(user_input='l')
    
    def test_validate_if_negative_number(self):
        """Test number validation when input is negative"""    
        # user_input = "-2"
        with self.assertRaises(ValueError):
            validate_if_number(user_input="-2")

    def test_validate_confirmation(self):
        """Test confirmation input if not y or n"""
        # user_input = 0
        with self.assertRaises(ValueError):
            validate_confirmation(user_input='0')

    def test_validate_confirmation_if_no(self):
        """Test if program exits if input == n"""
        # user_input = "n"
        with self.assertRaises(SystemExit) as error:
            validate_confirmation(user_input='n')
            self.assertEqual(error.exception.code, 1)

    def test_validate_budget(self):
        """Test validation when budget is lower than item price"""
        budget = 10
        item_price = 20
        with self.assertRaises(ValueError):
            validate_budget(budget, item_price)

    def test_validate_attempts(self):
        """Test validation when attempts are equal to or higher than 3"""
        attempts = 4
        with self.assertRaises(Exception):
            validate_attempts(attempts)

    def test_validate_if_not_empty(self):
        """Test validation when input is an empty string"""
        with self.assertRaises(ValueError):
            validate_if_not_empty(user_input='')

    @patch('builtins.input', return_value='2')
    def test_make_selection_when_input_valid(self, mock_input):
        """Test if selection is valid"""
        result = make_selection(self.item_list)
        self.assertEqual(result, {'kettle': 25})
            
    # @patch('builtins.input', return_value = '9')
    # @patch("shop.make_selection", InterruptedError)
    # def test_make_selection_when_input_invalid(self, mock_input):
    #     """Test if selection is valid"""
    #     make_selection(self.item_list)
    #     self.assertRaises(ValueError)        


if __name__ == '__main__':
    unittest.main()
