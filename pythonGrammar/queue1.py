
# size : 10
# -1 -1 3 4 5 6 7 8 9 10
# 0 1 2 3 4 5 6 7   8 10 % 10 -> rear -> 0
# quque[rear] = element


class queue:
    def __init__(self, size):
        self.size = size
        self.filled = 0
        self.empty = True
        self.full = False

        self.queue = []
        self.front = None
        self.rear = None

        for i in range(self.size):
            self.queue.append(None)


    def add(self,element):
        if self.front is None: # queue 가 비어있을때:
            self.front = 0
            self.rear = 1
            self.queue[0] = element
        else:
            self.queue[self.rear] = element
            self.rear += 1
            self.rear %=self.size


    def pop(self):
        # if queue is empty
        if self.front == None:
            print("The queue is empty, nothing to dequeue")
            return None
        #else
        else:
            self.front += 1
            self.front %= self.size
            return self.queue[self.front-1]

    def isEmpty(self):
        if self.front is None or self.front == self.rear:
            return True
        else:
            return False
    def getSize(self):
        return self.rear - self.front

    def getAll(self):
        return self.queue[self.front:self.rear]

    def printAll(self):
        for i in range(self.front,self.rear):
            print(self.queue[i])

