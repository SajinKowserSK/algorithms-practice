from models import BinaryNode

a_node = BinaryNode("A")
b_node = BinaryNode("B")
c_node = BinaryNode("C")
d_node = BinaryNode("D")
e_node = BinaryNode("E")

root = a_node
root.left = b_node
root.right = c_node
root.right.right = d_node
root.right.left = e_node

# preorder traversal
def traverse(root, target):
    if root is None:
        return False

    if root.data == target.data:

        return True

    left = traverse(root.left, target)
    right = traverse(root.right, target)

    if left or right:
        return True

    else:
        return False



def lca(root, n1, n2):
    if root is None or n1 is None or n2 is None:

        return None
    # if n2 is a child of n1
    if traverse(n1, n2):
        return n1

    # if n1 is a child of n2
    elif traverse(n2, n1):
        return n2


    else:

        # if left child is n1/n2 and right child is other
        if traverse(root.left, n1) and traverse(root.right, n2) \
                or traverse(root.right, n1) and traverse(root.left, n2):
            return root

        # if both in left
        elif traverse(root.left, n1) and traverse(root.left, n2):
            return lca(root.left, n1, n2)

        # if both in right
        else:
            return lca(root.right, n1, n2)


ans = lca(a_node, c_node, b_node)
print(ans.data)