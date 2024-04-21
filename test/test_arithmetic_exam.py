import unittest
from unittest.mock import patch
import pytest

from exam.arithmetic_exam import ArithmeticExam


class TestArithmeticExam(unittest.TestCase):

    #  The method should correctly evaluate a simple arithmetic expression and print the result.
    def test_evaluate_arithmetic_expression(self):
        with patch('builtins.input', return_value='2+2') as mock_input:
            with patch('builtins.print') as mock_print:
                ArithmeticExam.main()
                mock_input.assert_called_once()
                mock_print.assert_called_once_with(4)

    #  The method should raise a SyntaxError if the input is not a valid arithmetic expression.
    def test_invalid_arithmetic_expression(self):
        with patch('builtins.input', return_value='2+*2'):
            with pytest.raises(SyntaxError):
                ArithmeticExam.main()

    #  The method should raise a ZeroDivisionError if the input contains division by zero.
    def test_division_by_zero(self):
        with patch('builtins.input', return_value='2/0'):
            with pytest.raises(ZeroDivisionError):
                ArithmeticExam.main()
