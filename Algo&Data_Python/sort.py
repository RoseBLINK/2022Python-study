import random

def insertionSort(arr):
    s = 0
    std = []
    i = 1
    while i < len(arr):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if key > arr[j]:
                j -=1
                continue
            if key < arr[j]:
                arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
        i += 1
    print(arr)


def bubbleSort(arr):
    s = 0
    count = 0

    while count < len(arr):
        s = 0
        while s < len(arr)-1-count:
            if arr[s] > arr[s+1]:
                temp = arr[s]
                arr[s] = arr[s+1]
                arr[s+1] = temp
            s += 1
        count += 1
    return arr

def selectionSort(arr) :
    s = 0
    small = arr[s]
    count = 0

    while count < len(arr):
        s = count
        while s < len(arr) - 1:
            if small > arr[s+1]:
                small = arr[s+1]
                arr[s] = small
            s += 1
        count += 1

    return arr

def sort(arr):
    start = 0
    last = len(arr)
    while True:
        if arr[start] > arr[last]:
            temp = arr[start]
            arr[start] = arr[last]
            arr[last] = temp
        last -= 1
    return arr

def mergeSort(left,right,arr) :

    if left < right and  left:
        mid = int((left + right) / 2)
        print(arr[left:mid],arr[mid:right+1])
        leftArr = mergeSort(left,mid,arr[left:mid])
        rightArr = mergeSort(mid,right+1,arr[mid:right+1])
        return merge(leftArr,rightArr)
    else:
        arr


def merge(leftArr,rightArr):
    newArr = []
    l = 0
    r = 0
    while l < len(leftArr) and r < len(rightArr):
        if leftArr[l] < rightArr[r]:
            newArr.append(leftArr[l])
            l += 1
        elif (len(leftArr) == l) or leftArr[l] > rightArr[r]:
            newArr.append(rightArr[r])
            r += 1
    newArr += leftArr[l:]
    newArr += rightArr[r:]

    return newArr


def mergeNew(left,right,arr):
    mid = (left+right)//2

    l = left
    r = mid+1
    temp = []
    while l < mid and r < right:
        if arr[l] > arr[r]:
             temp.append(arr[r])
             r+=1
        else:
            temp.append(arr[l])
            l+=1
    return

# mergeNew(2,8,[])
def mergeSort(arr):
    if len(arr)<2:
        return arr

    mid = len(arr) // 2

    leftArr = mergeSort(arr[:mid])
    rightArr = mergeSort(arr[mid:])

    return merge(leftArr,rightArr)

def quickSort(arr):
    #퀵소트
    #피봇을 정하고 그것보다 작은것들은 왼쪽으로, 큰건 오른쪽으로
    if len(arr) <= 1:
        return arr

    left = []
    right =[]
    pivot = arr[len(arr) // 2]

    for data in arr:
        if data < pivot:
            left.append(data)
        elif data > pivot:
            right.append(data)
    pvList = []
    pvList.append(pivot)

    return quickSort(left) + pvList + quickSort(right)

a = [5, 9 ,6 ,8 ,7 ,2]
print(quickSort(a))

# def test(arr):
#     arr[2] = 1
#     return arr


# print(merge([1],[2]))
# merge([2,4,5],[1,3])
# arr = []
# for i in range(10):
#     arr.append(random.randint(1,100))
# # print(mergeSort(arr))
# print(mergeNew(2,5,arr))
#
# #
# # print(arr)
# # print(bubbleSort(arr))
# # print(arr)
# # print(selectionSort(arr))
#
# arr1 = [8,5, 6,2,4]
#
# # insertionSort(arr1)
# print(arr1[0:2])

# print(arr)

# test(arr)

# print(arr)

# print(merge([1,3,5,7],[2,4,6,8]))

     # 1 2 3 5 4  6 8 7 9
# 1 회차
# 5 9 2 3 4 1 7 8
# 2 회차
# 5 2 9 3 4 1 7 8
# 2 5 9 3 4 1 7 8
# 3 회차
# 2 5 3 9 4 1 7 8
# 2 3 5 9 4 1 7 8




# 5 9 2 3 4 1 7 8
# 5 9 2 3 4 1 7 8
# 5 9 2 3 4 1 7 8
# 1 5 9 2 3 4 7 8
# 1 4 5 9 2 3 7 8
# 1 4 3 5 9 2 7 8
# 1 4 3 2 5 9 7 8
# 1 2 4 3 5 9 7 8
# 1 2 3 4 5 9 7 8
# 1 2 3 4 5 8 7 9
# 1 2 3 4 5 7 8 9