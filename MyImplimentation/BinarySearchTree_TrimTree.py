class Node():
    def __init__(self, value):
        self.value = value
        self.right, self.left = None, None


def trimTree(tree, minval, maxval):
    if not tree:
        return None

    tree.left = trimTree(tree.left, minval, maxval)
    tree.right = trimTree(tree.right, minval, maxval)

    if minval <= tree.value <= maxval:
        return tree

    if tree.value < minval:
        return tree.right

    if tree.value > maxval:
        return tree.left


def printTree(tree):
    if tree != None:
        printTree(tree.left)
        print tree.value
        printTree(tree.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.left.left.left = Node(6)
root.right.right.right = Node(7)

tt = (trimTree(root, 1, 5))
printTree(tt)

