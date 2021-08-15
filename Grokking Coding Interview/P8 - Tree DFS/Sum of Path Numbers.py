class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    if root is None:
        return -1

    allPaths = []
    lst = []
    pSum = 0

    helper(root, lst, allPaths)

    totalSum = 0

    for path in allPaths:
        pathStr = ""
        for node in path:
            pathStr += str(node)

        totalSum += int(pathStr)
    return totalSum


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
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
