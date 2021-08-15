class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if root is None:
        return False

    allPaths = []
    lst = []
    helper(root, lst, allPaths)

    for path in allPaths:
        if len(path) == len(sequence):
            x = 0
            found = True
            for x in range(len(sequence)):
                if sequence[x] != path[x]:
                    found = False
                    break

            if found:
                return True

    return False


def helper(root, lst, allPaths):
    if root is not None and root.left is None and root.right is None:
        lst.append(root.val)

        allPaths.append(lst.copy())

        lst.pop(-1)

    elif root is not None:
        lst.append(root.val)
        helper(root.left, lst, allPaths)
        helper(root.right, lst, allPaths)

        lst.pop(-1)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
