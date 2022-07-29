class Calculator:
    def __init__(self):
        self.a = int(input('Введiть перше число:'))
        self.sign = input('Введiть знак:')
        self.b = int(input('Введiть друге число:'))
        self.start()

    def start(self):
        if self.sign == '+':
            self.sum(self.a, self.b)
        elif self.sign == '-':
            self.subtract(self.a, self.b)
        elif self. sign == '*':
            self.multiply(self.a, self.b)
        elif self.sign == '/':
            self.divide(self.a, self.b)
        else:
            print('Невiрний знак!!!')

    def sum(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

    def multiply(self, a, b):
        print(a * b)

    def divide(self, a, b):
        try:
            print(a / b)
        except ZeroDivisionError:
            print('Дiллення на 0 заборонено!!')





















       # if b == 0:
           # print('Не можна подiлити на 0')
        #else:
          #  print(a / b)


while True:
    Calculator()
