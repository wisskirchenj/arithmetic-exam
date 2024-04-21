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
    def test_generate_task_level_1(self, operator, operands, task, result, mock_choice, mock_randint):
        mock_choice.return_value = operator
        mock_randint.side_effect = operands
        task_generator = TaskGenerator()
        self.assertEqual(task, task_generator.generate_task(1))
        self.assertEqual(result, task_generator.get_result())

    @parameterized.expand([
        [12, 144],
        [29, 841],
        [20, 400]
    ])
    @patch('random.randint')
    def test_generate_task_level_2(self, operand, result, mock_randint):
        mock_randint.return_value = operand
        task_generator = TaskGenerator()
        self.assertEqual(str(operand), task_generator.generate_task(2))
        self.assertEqual(result, task_generator.get_result())
