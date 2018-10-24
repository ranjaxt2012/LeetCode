class Node():
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


def printLevelOrder(root):
    tree_height = get_tree_height(root, 0)
    for level in range(1, tree_height + 1):
        printbylevel(root, level)
        print ""


def get_tree_height(node, max_height):
    if node == None:
        return max_height
    else:
        lh = get_tree_height(node.left, max_height + 1)
        rh = get_tree_height(node.right, max_height + 1)
        return max(lh, rh)

def printbylevel(root, level):
    if root == None:
        return None
    elif level == 1:
        print root.value,
    else:
        printbylevel(root.left, level - 1)
        printbylevel(root.right, level - 1)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
printLevelOrder(root)
