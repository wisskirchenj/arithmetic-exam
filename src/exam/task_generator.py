import random


class TaskGenerator:

    def __init__(self):
        self.task: str = ''
        self.level = 0

    def generate_task(self, level: int) -> str:
        self.level = level
        left = self.random_operand(level)
        if level == 1:
            right = self.random_operand(level)
            operator = self.random_operator()
            self.task = f'{left} {operator} {right}'
        else:
            self.task = f'{left}'
        return self.task

    def get_result(self) -> int:
        return eval(self.task) if self.level == 1 else eval(f'{self.task} ** 2')

    @staticmethod
    def random_operand(level: int) -> int:
        return random.randint(2, 9) if level == 1 else random.randint(11, 29)

    @staticmethod
    def random_operator() -> str:
        return random.choice(['+', '-', '*'])
