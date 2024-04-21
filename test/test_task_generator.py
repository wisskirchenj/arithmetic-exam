import unittest
from unittest.mock import patch
from parameterized import parameterized

from exam.task_generator import TaskGenerator


class TestTaskGenerator(unittest.TestCase):

    @parameterized.expand([
        ['+', [2, 3], '2 + 3', 5],
        ['-', [2, 3], '2 - 3', -1],
        ['*', [7, 8], '7 * 8', 56],
        ['*', [7, 0], '7 * 0', 0]
    ])
    @patch('random.randint')
    @patch('random.choice')
    def test_generate_task(self, operator, operands, task, result, mock_choice, mock_randint):
        mock_choice.return_value = operator
        mock_randint.side_effect = operands
        task_generator = TaskGenerator()
        task_generator.generate_task()
        self.assertEqual(task, task_generator.get_task())
        self.assertEqual(result, task_generator.get_result())
