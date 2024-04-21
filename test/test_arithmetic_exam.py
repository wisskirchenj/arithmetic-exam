import unittest
from unittest.mock import patch, call

from exam.arithmetic_exam import ArithmeticExam, get_valid_number_input
from exam.task_generator import TaskGenerator


class TestArithmeticExam(unittest.TestCase):

    @patch.object(TaskGenerator, 'get_result', return_value=12)
    @patch.object(TaskGenerator, 'generate_task', return_value='3 * 4')
    @patch('builtins.print')
    @patch('builtins.input', return_value='12')
    def test_correct_answer(self, mock_input, mock_print, mock_get_task, mock_get_result):
        ArithmeticExam().exam_task()
        mock_print.assert_has_calls([call('3 * 4'), call('Right!')])

    @patch.object(TaskGenerator, 'get_result', return_value=12)
    @patch.object(TaskGenerator, 'generate_task', return_value='3 * 4')
    @patch('builtins.print')
    @patch('builtins.input', return_value='13')
    def test_wrong_answer(self, mock_input, mock_print, mock_get_task, mock_get_result):
        ArithmeticExam().exam_task()
        mock_print.assert_has_calls([call('3 * 4'), call('Wrong!')])

    @patch.object(TaskGenerator, 'get_result', return_value=12)
    @patch.object(TaskGenerator, 'generate_task', return_value='3 * 4')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_main_loop(self, mock_input, mock_print, mock_get_task, mock_get_result):
        mock_input.side_effect = ['abc', '13', '12', '12', '12', '12']
        ArithmeticExam().main()
        mock_print.assert_any_call('Incorrect format.')
        mock_print.assert_any_call('Right!')
        mock_print.assert_any_call('Wrong!')
        mock_print.assert_called_with('Your mark is 4/5.')

    @patch('builtins.print')
    @patch('builtins.input')
    def test_get_valid_number_input(self, mock_input, mock_print):
        mock_input.return_value = '12'
        self.assertEqual(12, get_valid_number_input())
        mock_print.assert_not_called()

    @patch('builtins.print')
    @patch('builtins.input')
    def test_get_with_invalid_number_input(self, mock_input, mock_print):
        mock_input.side_effect = ['1+2', 'abc', '13']
        self.assertEqual(13, get_valid_number_input())
        self.assertEqual(2, mock_print.call_count)
