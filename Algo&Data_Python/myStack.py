class myStack:
    def __init__(self, size):
        self.top = 0 #idx
        self.size = size

        self.stack = []
        for i in range(self.size):
            self.stack.append(None)

    def push(self, e):
        self.stack[self.top] = e
        self.top += 1
        return self.stack[:self.top]

    def pop(self):
        if self.top <= 0:
            return False
        else:
            self.stack.pop()
            self.top -= 1
            return self.stack[self.top]

    def topIDX(self):
        return self.top

    def topEle(self):
        return self.stack[self.top]

    def all(self):
        return self.stack[:self.top]



