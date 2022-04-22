
class Node:
    def __init__(self, left, right, value: str):
        self.left = left
        self.right = right
        self.value = value


root = Node(Node(None, None,"1"), Node(Node(None, None, "3"), Node(None, None, "4"), "6"), "0")


def preOrder(root: Node):
    if not root:
        return ""
    return "{value}{first}{second}".format(value=root.value, first=preOrder(root.left), second=preOrder(root.right))

def preOrderNonRecursive(root: Node):

    string = str()
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        string = string + node.value
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return string


print(preOrder(root))
print(preOrderNonRecursive(root))


def postOrder(root: Node):
    if not root:
        return ""
    return "{first}{second}{value}".format(value=root.value, first=postOrder(root.left), second=postOrder(root.right))

print(postOrder(root))

def inOrder(root: Node):
    if not root:
        return ""
    return "{first}{value}{second}".format(value=root.value, first=inOrder(root.left), second=inOrder(root.right))

def inOrderNonRecursive(root: Node):
    string = str()
    stack = []
    node = root
    while True:
        if node:
            stack.append(node)
            node = node.left
        elif not node and len(stack) > 0:
            node = stack.pop(-1)
            string = string + node.value
            node = node.right
        else:
            break

    return string

print(inOrder(root))
print(inOrderNonRecursive(root))

def revertTree(root: Node):
    if not root:
        return
    left= root.left
    root.left = root.right
    root.right = left
    revertTree(root.right)
    revertTree(root.left)
    return root

print(preOrder(root))
print(preOrder(revertTree(root)))