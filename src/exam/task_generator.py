import random


class TaskGenerator:

    def __init__(self):
        self.task: str = ''

    def generate_task(self):
        left = self.random_operand()
        right = self.random_operand()
        operator = self.random_operator()
        self.task = f'{left} {operator} {right}'

    def get_task(self) -> str:
        return self.task

    def get_result(self) -> int:
        return eval(self.task)

    @staticmethod
    def random_operand() -> int:
        return random.randint(2, 9)

    @staticmethod
    def random_operator() -> str:
        return random.choice(['+', '-', '*'])
