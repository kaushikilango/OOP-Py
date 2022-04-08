class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            inorder(root.left)
            print(root.data)
            inorder(root.right)

    def postorder(self, root):
        if root:

            postorder(root.right)
            print(root.data)
            postorder(root.left)

    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)


t = Tree()
x1 = Node(data=10)
x2 = Node(data=11)
x3 = Node(data=12)
x4 = Node(data=13)
x5 = Node(data=14)
x6 = Node(data=19)
x7 = Node(data=20)
x8 = Node(data=15)
x9 = Node(data=16)
x10 = Node(data=17)
x11 = Node(data=18)
x12 = Node(data=21)
x13 = Node(data=22)

t.root = x1
x1.left = x2
x2.right = x3
x2.right = x5
x2.left = x4
x3.left = x6
x3.right = x7
x4.right = x9
x4.left = x8
x5.left = x10
x5.right = x11
x7.left = x12
x7.right = x13
t.preorder(t.root)
