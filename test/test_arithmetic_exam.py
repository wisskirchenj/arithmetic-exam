import unittest
from unittest.mock import patch, call

from exam.arithmetic_exam import ArithmeticExam
from exam.task_generator import TaskGenerator


class TestArithmeticExam(unittest.TestCase):

    @patch.object(TaskGenerator, 'get_result', return_value=12)
    @patch.object(TaskGenerator, 'get_task', return_value='3 * 4')
    @patch('builtins.print')
    @patch('builtins.input', return_value='12')
    def test_correct_answer(self, mock_input, mock_print, mock_get_task, mock_get_result):
        ArithmeticExam().main()
        mock_print.assert_has_calls([call('3 * 4'), call('Right!')])

    @patch.object(TaskGenerator, 'get_result', return_value=12)
    @patch.object(TaskGenerator, 'get_task', return_value='3 * 4')
    @patch('builtins.print')
    @patch('builtins.input', return_value='13')
    def test_wrong_answer(self, mock_input, mock_print, mock_get_task, mock_get_result):
        ArithmeticExam().main()
        mock_print.assert_has_calls([call('3 * 4'), call('Wrong!')])
