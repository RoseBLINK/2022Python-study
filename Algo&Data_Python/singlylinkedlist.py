class Node():
    def __init__(self,e):
        self.element = e
        self.next = None


class SLL():

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def getFirst(self):
        return self.head.element

    def getLast(self):
        return self.tail.element

    def getAfter(self, idx):
        return

    def removeLast(self):

        if self.head == None:
            return
        else:
            cur = self.head
            while cur.next.next != None:
                cur = cur.next
            cur.next = None

    def removeFirst(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next

    def insert(self, e):
        if self.head is None: # 빈 링크드리스트 일경우
            node = Node(e)
            self.head = node
            self.tail = node
        else: # 아닌 경우
            cur = self.head
            while cur.next != None:
                cur = cur.next
            node = Node(e)
            cur.next = node

    def insertWithTail(self,e):
        node = Node(e)
        self.tail.next = node
        self.tail = self.tail.next

    # 구현
    def insertAfter(self, idx, e):
        node = Node()
        node.element = e
        node.idx = idx

    def removeFirst(self):
        return


    def remove(self, idx):
        if idx == 0:
            self.head = self.head.next
        else:
            i = 0
            cur = self.head
            while i < idx-1: # idx : 2
                cur = cur.next
                i+=1
            cur.next = cur.next.next
        return


    def size(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def printAll(self):
        cur = self.head
        while cur != None:
            print(cur.element)
            cur = cur.next

class linkedStack:
    def __init__(self):
        self.size = 0
        self.head = None
    def pop(self):

        if self.head == None:
            return
        else:
            cur = self.head
            while cur.next.next != None:
                cur = cur.next
            cur.next = None

    def top(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next

        return cur.element

    def push(self, e):
            if self.head is None: # 빈 링크드리스트 일경우
                node = Node(e)
                self.head = node
                self.tail = node
            else: # 아닌 경우
                cur = self.head
                while cur.next != None:
                    cur = cur.next
                node = Node(e)
                cur.next = node
class linkedQueue():
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, e):
        if self.head is None: # 빈 링크드리스트 일경우
            node = Node(e)
            self.head = node
            self.tail = node
        else: # 아닌 경우
            cur = self.head
            while cur.next != None:
                cur = cur.next
            node = Node(e)
            cur.next = node

    def dequeue(self):
        if self.head == None:
            return
        else:
            cur = self.head
            self.head = cur.next
            cur = None

    def printAll(self):
        cur = self.head
        while cur != None:
            print(cur.element)
            cur = cur.next
            





if __name__ == "__main__":
    linkedlist = SLL()
    linkedlist.insert("A")
    # linkedlist.printAll()
    linkedlist.insert("B")
    # linkedlist.printAll()
    linkedlist.insert("C")
    linkedlist.insert("D")
    linkedlist.insert("E")
    linkedlist.insert("F")
    linkedlist.printAll()
    print("--------------")
    linkedlist.removeLast()
    linkedlist.printAll()
    # print(linkedlist.isEmpty()) # true
    # linkedlist.insertAfter(0,"A")
    # linkedlist.insertAfter(1,"B")
    # linkedlist.insertAfter(2,"C")
    # linkedlist.insertAfter(3,"D")
    # print(linkedlist.getFirst()) # "A"
    # print(linkedlist.getLast()) # "D"
    # linkedlist.remove(2) # C
    # print(linkedlist.getAfter(1)) # D
    # print(linkedlist.size()) # 3
    # print(linkedlist.isEmpty())  # false

# linkedlist -> stack, queue
