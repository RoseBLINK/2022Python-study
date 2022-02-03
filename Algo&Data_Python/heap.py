import sys

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
    def pop(self):
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self.heapify(1)

    def heapify(self, idx):
        leftChild = idx * 2
        rightChild = idx * 2 + 1


        #예외처리
        #the hardest

        if leftChild > self.size :
            leftChildValue = sys.maxsize
        else:
            leftChildValue = self.heap[leftChild]

        if rightChild > self.size:
            rightChildValue = sys.maxsize
        else:
            rightChildValue = self.heap[rightChild]


        if self.heap[idx] < leftChildValue and self.heap[idx] < rightChildValue: # 최대 heap 만족
            return
        elif leftChildValue < self.heap[idx] and leftChildValue < rightChildValue: # left 가 클때
            self.heap[leftChild], self.heap[idx] = self.heap[idx], leftChildValue
            self.heapify(leftChild)
        else: # right 가 클때
            self.heap[rightChild], self.heap[idx] = self.heap[idx], rightChildValue
            self.heapify(rightChild)
            
            
        
            

# Github 정리해서 올리기
# 퀵소트 구현
# 머지소트 다른 방식으로 구현( 배열 자르기 x, 배열은 그대로 index 를 통해 구현하기 )

heap = MinHeap()

heap.push(4)

heap.push(6)
heap.push(7)
heap.push(9)
heap.push(10)
heap.push(3)
heap.push(2)
# print(heap.top()) # 2
heap.push(1)
# print(heap.top()) # 1
heap.print()

heap.pop()
heap.print()
heap.pop()
heap.print()