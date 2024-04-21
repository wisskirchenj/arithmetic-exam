from exam.task_generator import TaskGenerator


class ArithmeticExam:

    def __init__(self):
        self.task_generator = TaskGenerator()

    def main(self):
        self.task_generator.generate_task()
        print(self.task_generator.get_task())
        user_input = input()
        print('Right!' if self.task_generator.get_result() == int(user_input) else 'Wrong!')


if __name__ == '__main__':
    ArithmeticExam().main()
