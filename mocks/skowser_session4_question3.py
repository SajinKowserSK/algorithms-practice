class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = BinaryNode(3)
root.right = BinaryNode(2)
root.left = BinaryNode(5)
root.left.left = BinaryNode(1)
root.left.right = BinaryNode(4)
root.right.left = BinaryNode(6)

root2 = BinaryNode(3)
root2.left = BinaryNode(1)
root2.left.right = BinaryNode(2)
root2.left.left = BinaryNode(0)

root2.right = BinaryNode(5)
root2.right.left = BinaryNode(4)
root2.right.right = BinaryNode(6)

def is_valid_bst(root):
    if root is None:
        return None

    arr = inorder(root, [])
    for x in range(0, len(arr)-1):
        if arr[x+1] < arr[x]:
            return False

    return True

def inorder(root, lst):
    if root is not None:
        inorder(root.left, lst)
        lst.append(root.val)
        inorder(root.right, lst)

        return lst

print(inorder(root, []))
print(is_valid_bst(root))

print(is_valid_bst(root2))


