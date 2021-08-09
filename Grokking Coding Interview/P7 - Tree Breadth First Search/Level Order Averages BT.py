class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    q = []
    q.append(root)

    while q:
        lvlSize = len(q)

        curr_sum = 0

        for node in range(lvlSize):
            popped = q.pop(0)

            if popped.left:
                q.append(popped.left)

            if popped.right:
                q.append(popped.right)

            curr_sum += popped.val

        avg = curr_sum / lvlSize
        result.append(avg)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()







