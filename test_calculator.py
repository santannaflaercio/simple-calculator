import unittest
from unittest.mock import patch
from calculator import calculate


class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '3'])
    @patch('builtins.print')
    def test_addition(self, mock_print, mock_input):
        calculate('1')
        mock_print.assert_any_call('2.0 + 3.0 = 5.0\n')

    @patch('builtins.input', side_effect=['5', '3'])
    @patch('builtins.print')
    def test_subtraction(self, mock_print, mock_input):
        calculate('2')
        mock_print.assert_any_call('5.0 - 3.0 = 2.0\n')

    @patch('builtins.input', side_effect=['2', '3'])
    @patch('builtins.print')
    def test_multiplication(self, mock_print, mock_input):
        calculate('3')
        mock_print.assert_any_call('2.0 * 3.0 = 6.0\n')

    @patch('builtins.input', side_effect=['10', '2'])
    @patch('builtins.print')
    def test_division(self, mock_print, mock_input):
        calculate('4')
        mock_print.assert_any_call('10.0 / 2.0 = 5.0\n')


if __name__ == '__main__':
    unittest.main()
