class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = BinaryNode(1)
root.right = BinaryNode(2)
root.right.right = BinaryNode(5)
root.right.right.right = BinaryNode(6)
root.right.right.left = BinaryNode(3)
root.right.right.left.right = BinaryNode(4)


def print_level_order(root):
    if root is not None:
        queue = []
        queue.append(root)
        while len(queue) > 0:
            popped = queue.pop(0)
            print(popped.val)
            if popped.left != None:
                queue.append(popped.left)

            if popped.right != None:
                queue.append(popped.right)

print_level_order(root)

