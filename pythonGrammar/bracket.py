
# { {} ( ) } -> true
# {(}) -> false
# [[[())]]] -> false

class Bracket():
    def __init__(self):
        self.open = []
        self.close = []

    def countOpen(self, e):
        for i in range(len(e)):
            if e[i] in ['{','[','(']:
                self.open.append(e[i])

    def countClose(self, e):
        for i in range(len(e)):
            if e[i] in ['}',']',')']:
                self.close.append(e[i])

    def compare(self):
        print("open len : ",len(self.open))
        print("close len : ",len(self.close))
        dic = {'{': '}', '[': ']','(': ')' }
        for i in range(len(self.open)):
            if dic[self.open[i]] == self.close[len(self.close)-i-1]:
                continue
            else:
                return False
        return True

    def getInput(self):
        input1 = input()
        return input1

bracket = Bracket()
e = bracket.getInput()

bracket.countOpen(e)
bracket.countClose(e)
if bracket.compare():
    print("true")
else:
    print("false")