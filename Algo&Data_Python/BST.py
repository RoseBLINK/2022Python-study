class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST():
    def __init__(self):
        self.height = 0
        self.root = None

    def add(self,e):
        if self.root is None:
            self.root = Node(e)
        else:
            cur = self.root
            while True:
                if cur.data > e:
                    if cur.left is None:
                        cur.left = Node(e)
                        break
                    cur = cur.left
                elif cur.data < e:
                    if cur.right is None:
                        cur.right = Node(e)
                        break
                    cur = cur.right

    def search(self,e):
        if self.root is None:
            return False
        cur = self.root
        while cur.left is not None or cur.right is not None:
            if cur.data > e:
                if cur.left is None:
                    return False
                cur = cur.left
            elif cur.data < e:
                if cur.right is None:
                    return False
                cur = cur.right
            else:
                return True
    # Binary Tree -> Node 코드
    # def binary(self,start, end):
    #     mid = start + end
    #     if start - end < 1:
    #         return
    #     else:
    #         self.add(self.l[mid])
    #         self.binary(start,end)
    #
    # 1 100 50
    # def build(self, l):
    #     l.sort
    #     idx = len(l)//2
    #     self.add(l[idx])




a = BST()

arr = [2,3,5,9,11,12,20,22,24,26,29,30,31]
for element in arr:
    a.add(element)
print(a.search(5))
print(a.search(9))
print(a.search(1))

# a.build([2,3,5,9,11,12,20,22,24,26,29,30,31])
