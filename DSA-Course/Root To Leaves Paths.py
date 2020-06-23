from models import *

# O(n) time complexity
# O(h) space complexity on recursion stack (never storing all the nodes in path,
# just storing deepest one in worst case)
root = createTree([4, 2, 6, 1, 1.5, 5, 7])

def printPaths(root, path):
    if root is None:
        return

    path.append(root.getVal())

    if root.isLeaf():
        print(path)

    printPaths(root.getLeft(), path)
    printPaths(root.getRight(), path)
    path.pop()

print(printPaths(root, []))
