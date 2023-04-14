import unittest
from foundation_assessment2_task1 import check_if_isogram


class TestCheckIfIsogram(unittest.TestCase):
    def test_input(self):
        word = "isogram"
        self.assertEqual(check_if_isogram(word), True)

    def test_input2(self):
        word = "uncopyrightable"
        self.assertEqual(check_if_isogram(word), True) 
    
    def test_input3(self):
        word = "ambidextrously"
        self.assertEqual(check_if_isogram(word), True)
    
    def test_input4(self):
        word = "where"
        self.assertEqual(check_if_isogram(word), False)


if __name__ == '__main__':
    unittest.main()