class Node():
    def __init__(self,e):
        self.element = e
        self.childs = []

    def insert(self,e):
        if len(self.childs) < 3:
            self.childs.append(Node(e))
            return
        else:
            for child in self.childs:
                if child.insert(e):
                    break


    def printAll(self):
        print(self.element)
        for child in self.childs:
            child.printAll()

class Tree():
    def __init__(self):
        self.height = 0
        self.root = None

    def insert(self,cur,e):
        if self.root is None:
            self.height += 1
            self.root = Node(e)
        else:
            if len(cur.child) < 3:
                cur.child.append(Node(e))
            else:
                for child in cur.child:
                    self.insert(child,e)



    def printAll(self,cur):
        print(cur.element)
        for child in cur.child:
            self.printAll(child)

# tree = Tree()
# tree.insert(None,1)
# print("root",tree.root.element)
# for i in range(2,15):
#     print("root",tree.root.element)
#     tree.insert(tree.root, i)
# tree.printAll(tree.root)

root = Node(1)
for i in range(2,15):
    root.insert(i)
root.printAll()


# def selectionSort(arr) :
#     count = 0
#
#     while count < len(arr):
#         s = count
#         small = arr[s]
#         while s < len(arr) - 1:
#             if small > arr[s+1]:
#                 small = arr[s+1]
#                 smallIdx = s+1
#             s += 1
#         temp = arr[smallIdx]
#         arr[s] = arr[smallIdx]
#         arr[smallIdx] = temp
#     count += 1
#
#     return arr