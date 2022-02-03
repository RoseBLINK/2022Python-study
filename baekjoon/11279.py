# 최대힙
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
#
# 입력
# 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
# 입력되는 자연수는 231보다 작다.

#진짜 뭔소린지 1도 모르겠음

# 인풋     아웃풋
# 13        0
# 0         2
# 1         1
# 2         3
# 0         2
# 0         1
# 3         0
# 2         0
# 1
# 0
# 0
# 0
# 0
# 0

import sys
import heapq

class MaxHeap:
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
            if self.heap[parent] < self.heap[idx]:
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
        if self.size == 0:
            return 0
        if self.size ==1:
            self.size -=1
            return self.heap.pop()
        temp = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self.heapify(1)
        return temp

    def heapify(self, idx):
        leftChild = idx * 2
        rightChild = idx * 2 + 1
        #예외처리

        if leftChild > self.size :
            leftChildValue = -1 - sys.maxsize
        else:
            leftChildValue = self.heap[leftChild]

        if rightChild > self.size:
            rightChildValue = -1 - sys.maxsize
        else:
            rightChildValue = self.heap[rightChild]


        if self.heap[idx] > leftChildValue and self.heap[idx] > rightChildValue: # 최대 heap 만족
            return
        elif leftChildValue > self.heap[idx] and leftChildValue > rightChildValue: # left 가 클때
            self.heap[leftChild], self.heap[idx] = self.heap[idx], leftChildValue
            self.heapify(leftChild)
        else: # right 가 클때
            self.heap[rightChild], self.heap[idx] = self.heap[idx], rightChildValue
            self.heapify(rightChild)

def main():
    n = int(sys.stdin.readline())
    i = 0
    heap = MaxHeap()
    while i < n:
        number = int(sys.stdin.readline())
        if number == 0:
            print(heap.pop())

        elif number > 0:
            heap.push(number)
        i += 1

# j = 0
#     while j < int(num):
#         if inputList[j] == 0:
#             # print(heap.pop())
#             if len(heapArr) == 0:
#                 print(0)
#             else:
#                 print(heapq.heappop(heapArr)[1])
#         elif inputList[j] > 0:
#             # heap.push(inputList[j])
#             heapq.heappush(heapArr,(-inputList[j],inputList[j]))
#
#         j += 1

main()