import sys

class Calculator:
    # self -> java this 같은 것
    # class 내의 지역변수 call 하기 위해서는 self.변수명 해야함
    def __init__(self,firstNumber,secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
        self.result = 0
    # 함수의 시작은 def(self,parameter1, parameter2):
    # 함수의 리턴 타입은 지정하지 않음
    # 리턴을 안하면 그냥 void임
    def add(self):
        print(self.firstNumber + self.secondNumber)
        self.result = self.firstNumber + self.secondNumber
        return

    def multiple(self):
        print(self.firstNumber * self.secondNumber)
        return

    def divide(self):
        print(self.firstNumber / self.secondNumber)
        return

    def minus(self):
        print(self.firstNumber - self.secondNumber)

    def print(self):
        print(self.result)





cal = Calculator(5,2)




1+2+4+5-30*10
