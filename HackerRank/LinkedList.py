
class Node:
    def __init__ (self, val, nextNode=None):
        self.value = val
        self.next = nextNode


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def addFront(self, data):
        curr = self.head
        self.head = Node(data, curr)
        self.size+=1
        return True

    def getData(self):
        return self.getValue()

    def printList(self):
        curr = self.head
        links = ""
        while curr != None:
            links = links + str(curr.value) + " "
            curr = curr.next
        print(links)

    def Sort(self):
        curr = self.head
        nxt = self.head.next
        for _ in range(self.size-1):
            while nxt != None:
                if curr.value > nxt.value:
                    temp = curr.value
                    curr.value = nxt.value
                    nxt.value= temp
                nxt = nxt.next

            curr = curr.next
            nxt = curr.next

    def search(self, num):
        curr = self.head
        while curr != None:
            if num == curr.value:
                print("Contains "+ str(num))
                return True
            curr = curr.next
        print("Does Not Contain " + str(num))
        return False

    def addBack(self, data):
        curr = self.head
        for _ in range(self.size-1):
            curr = curr.next
        curr.next = Node(data, None)
        self.size += 1



myList = LinkedList()

myList.addFront(12)
myList.addFront(14)
myList.addFront(24)
myList.addFront(64)
myList.addFront(15)
myList.addFront(10)
myList.addFront(11)

myList.printList()
print(myList.size)
myList.Sort()
myList.printList()

myList.search(13)
myList.addBack(9)
myList.printList()

myList.Sort()
myList.printList()



