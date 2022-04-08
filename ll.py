#linked list implementation

from platform import node


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self,):
        self.head = None

    def printlist(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            a = self.head
            while a is not None:
                print(f"{a.data}")
                a = a.next

    def push(self,data):
        n3 = Node(4)
        n3.next = self.head
        self.head = n3 

    def append(self,data):
        nl = Node(data)
        nl.next = None
        if self.head is None:
            self.head = nl
        else:
            last = self.head
            while (last.next):
                last = last.next
            last.next = nl
    def push_at_loc(self,prev,data):
        nx = Node(data)
        t = self.head
        while(t):
            if(t.data == prev):
                nx.next = t.next
                t.next = nx
            t = t.next

l1 = LinkedList()
n1 = Node(4)
n2 = Node(6)
n3 = Node(8)
n4 = Node(9)
l1.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
l1.push_at_loc(6,7)

l1.printlist()
