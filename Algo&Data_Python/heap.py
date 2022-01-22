class MinHeap:
    def __init__(self):
        self.size = 0
        self.root = None

        self.heap = [0]
    def push(self, data):
        self.heap.append(data)
        self.size += 1
        idx = self.size

        while idx != 1:
            parent = idx // 2
            if self.heap[parent] > self.heap[idx]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[idx]
                self.heap[idx] = temp
            idx = idx // 2

    def top(self):
        return self.heap[1]

    def print(self):
        i = 1
        while i < self.size+1:
            j = i
            result = ""
            while j < i * 2 and j < self.size+1 :
                result += str(self.heap[j])+" "
                j += 1
            print(result)
            i *= 2
    #def pop(self):

# Github 정리해서 올리기
# 퀵소트 구현
# 머지소트 다른 방식으로 구현( 배열 자르기 x, 배열은 그대로 index 를 통해 구현하기 )

heap = MinHeap()

heap.push(4)
heap.push(3)
heap.push(2)
# print(heap.top()) # 2
heap.push(1)
# print(heap.top()) # 1
heap.print()


