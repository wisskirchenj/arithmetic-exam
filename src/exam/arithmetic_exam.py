import re
from exam.task_generator import TaskGenerator
from exam.result_saver import ResultSaver


def get_valid_number_input(regex: str = r'[+-]?\d+$') -> int:
    while True:
        user_input = input()
        if re.match(regex, user_input):
            return int(user_input)
        print('Incorrect format.')


class ArithmeticExam:

    def __init__(self):
        self.task_generator = TaskGenerator()
        self.level = 0
        self.correct_answers = 0

    def exam_task(self):
        print(self.task_generator.generate_task(self.level))
        user_input = get_valid_number_input()
        correct = self.task_generator.get_result() == user_input
        print('Right!' if correct else 'Wrong!')
        if correct:
            self.correct_answers += 1

    def main(self):
        self.ask_level()
        for _ in range(5):
            self.exam_task()
        print(f'Your mark is {self.correct_answers}/5. Would you like to save the result? Enter yes or no.')
        if input() in ['yes', 'y', 'Yes', 'YES']:
            ResultSaver().save_result(self.correct_answers, self.level)

    def ask_level(self):
        print('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29''')
        self.level = get_valid_number_input(r'[12]')


if __name__ == '__main__':
    ArithmeticExam().main()