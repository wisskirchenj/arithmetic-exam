from exam.task_generator import TaskGenerator


def get_valid_number_input() -> int:
    while True:
        user_input = input()
        if user_input.lstrip('-+').isdigit():
            return int(user_input)
        print('Incorrect format.')


class ArithmeticExam:

    def __init__(self):
        self.task_generator = TaskGenerator()
        self.correct_answers = 0

    def exam_task(self):
        print(self.task_generator.generate_task())
        user_input = get_valid_number_input()
        correct = self.task_generator.get_result() == user_input
        print('Right!' if correct else 'Wrong!')
        if correct:
            self.correct_answers += 1

    def main(self):
        for _ in range(5):
            self.exam_task()
        print(f'Your mark is {self.correct_answers}/5.')


if __name__ == '__main__':
    ArithmeticExam().main()