import math
import random
class BinarySearch():
    def __init__(self):
        self.arr= []
        for i in range(100):
            self.arr.append(random.randint(1,1000))

        self.arr.append(770)
        self.arr.sort()
        print(self.arr)


    def search(self, e):
        start = 0
        end = len(self.arr)
        while start < end and end - start != 1:
            if (start + end)%2 == 0:
                mid = int((start + end)/2)
            else:
                mid = int((start + end + 1)/2)

            if self.arr[mid] < e:
                start = mid
            elif self.arr[mid] > e:
                end = mid
            else:
                return True

        return False

    # def searchRecur(self, start, end, e):
    #     mid = 0
    #     if (start + end) % 2 == 0:
    #         mid = int((start + end)/2)
    #     else:
    #         mid = int((start + end + 1)/2)
    #
    #
    #     if self.arr[mid] < e:
    #         return self.searchRecur(start, mid, e)
    #     elif self.arr[mid] > e:
    #         return self.searchRecur(mid, end, e)
    #     elif abs(start - end) == 1 or start == end:
    #         return False
    #     elif self.arr[mid] == e:
    #         return True

    def searchRecur(self, start, end, e):
        mid = 0
        if (start + end) % 2 == 0:
            mid = int((start + end)/2)
        else:
            mid = int((start + end + 1)/2)

        if abs(start - end) == 1 or start == end:
            return False
        elif self.arr[mid] == e:
            return True
        if self.arr[mid] < e:
            return self.searchRecur(start, mid, e)
        elif self.arr[mid] > e:
            return self.searchRecur(mid, end, e)

bs = BinarySearch()

# print(bs.search(100))
#
# print(bs.search(101))
# print(bs.search(102))
print(bs.searchRecur(0,100,103))
print(bs.searchRecur(0,100,770))