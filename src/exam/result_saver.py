class ResultSaver:

    path = 'results.txt'
    description = ['simple operations with numbers 2-9', 'integral squares of 11-29']

    def save_result(self, correct_answers: int, level: int):
        user_name = input('What is your name?\n')
        with open(self.path, 'a') as file:
            file.write(f'{user_name}: {correct_answers}/5 in level {level} ({self.description[level - 1]}).\n')
        print(f'The results are saved in "{self.path}".')