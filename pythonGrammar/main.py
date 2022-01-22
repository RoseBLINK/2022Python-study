import queue1
import myStack

stck = myStack.myStack(12)

stck.push(1)
stck.push(2)
stck.push(3)
stck.push(4)
stck.push(5)
stck.push(6)
stck.push(7)
print(stck.push(8))

print(stck.pop()) # 8
print(stck.pop()) # 7
print(stck.all())
print(stck.topIDX())
print(stck.topEle())
# que = queue.queue(100)
# 
# que.add(1)
# que.add(2)
# que.add(3)
# que.add(4)
# que.add(5)
# que.add(6)
# que.add(7)
# que.add(8)
# 
# print(que.pop()) # 1
# print("-----------")
# print(que.pop()) # 2
# print("-----------")
# print(que.getAll())
# print("-----------")
# print(que.getSize())
# print("-----------")
#que.printAll()