from models import *

root = createTree([4,2,6,3,5,5.5])

def getHeight(root, height):
    if root is None:
        return height

    height = height + 1
    leftSubTree = getHeight(root.getLeft(), height)
    rightSubTree = getHeight(root.getRight(), height)

    return max(leftSubTree, rightSubTree)

print(getHeight(root, -1))