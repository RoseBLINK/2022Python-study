class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, B, data):
        if self.size == 0:
            node = Node(data)
            self.root = node
            self.size += 1
        elif self.size > 0:
            node = Node(data)
            if B == "l" or "L":
                self.root.left = node
            elif B == "r" or "R":
                self.root.right = node
        else:
            return

    # def delete(self, data):
    #     if self.size == 0:
    #         return
    #     elif self.size > 0:

    def search(self, data):
        if self.size == 0:
            return
        elif self.size > 0:
            if self.root.data == data:
                return self.root.data
            else:
                return

    def inorder(self):
        return

