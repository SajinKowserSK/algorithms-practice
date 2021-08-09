class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    q = []
    q.append(root)
    start_left = True
    while q:
        lvlSize = len(q)
        curr_lvl = []

        for node in range(lvlSize):
            popped = q.pop(0)

            if popped.left:
                q.append(popped.left)

            if popped.right:
                q.append(popped.right)

            if start_left:
                curr_lvl.append(popped.val)

            else:
                curr_lvl.insert(0, popped.val)

        result.append(curr_lvl)
        if start_left:
            start_left = False

        else:
            start_left = True

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
