# input은 숫자와 * / - +
# input()
# Calculator 클래스 생성
# 계산하는 함수
# 결과값을 출력하는 함수

class calc:


    def __init__(self, input):
        self.input = input
        self.string = []

    def parse(self):
        self.string = self.input.split(' ')
        
    def calculate(self):
        i = 0
        a = self.string
# 1 + 2 - 4 * 3
        while i < len(a):
            if a[i] == "*":
                result = int(a[i-1]) * int(a[i+1])
                a[i] = result
                a.pop(i+1)
                a.pop(i-1)
            elif a[i] == "/":
                result = int(a[i-1]) / int(a[i+1])
                a[i] = result
                a.pop(i+1)
                a.pop(i-1)
            i+=1
        i=0
        while i < len(a):
            if a[i] == "-":
                result = int(a[i-1]) - int(a[i+1])
                a[i] = result
                a.pop(i+1)
                a.pop(i-1)
                i = i-1
            elif a[i] == "+":
                result = int(a[i-1]) + int(a[i+1])
                a[i] = result
                a.pop(i+1)
                a.pop(i-1)
                i = i-1
            i+=1
        print(a[0])



def get_input():
    str = input()
    return str

# str = get_input()

cal = calc("1 + 2 - 4 * 3")
cal.parse()
cal.calculate()