class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = 0 #idx
        self.size = 0

        # self.stack = []
        # for i in range(self.size):
        #     self.stack.append(None)

        #stack 코드를 메인으로 안에 linked list 코드 좀 섞으면

    def push(self, e):
            #노드 생성후 self.top 을 다음을 향하게
            #사이즈 + 1
            #self.next 도 다음을 향하게(top)
            n = Node()
            n.element = e
            self.size += 1
            self.top += 1
            n.next = self.top

    def pop(self):
        if self.top <= 0:
            return False
        else:
            cur = self.top - 2


    def topIDX(self):
        return self.top

    def topEle(self):
        return self.stack[self.top]

    def all(self):
        return self.stack[:self.top]



