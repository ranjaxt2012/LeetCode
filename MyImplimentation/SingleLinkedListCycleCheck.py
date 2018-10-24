class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, element):
        new_node = Node(element)

        if self.head == None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def printList(self):
        current = self.head
        while current:
            print current.value
            current = current.next


def checkCircularLoop(node):
    c1 = node
    c2 = node

    while c2.next != None:

        c1 = c1.next
        c2 = c2.next.next

        if c1 == c2:
            return True

    return False


def reverseList(head):
    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.next
        current.next = previous
        previous = current
        current = nextnode
    return previous




ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

ll.printList()

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a
print checkCircularLoop(a)

a.next = b
b.next = c
c.next = None
reverseList(ll)
ll.printList()
