class ArithmeticExam:

    @staticmethod
    def main():
        user_input = input()
        result = eval(user_input)
        print(result)


if __name__ == '__main__':
    ArithmeticExam().main()