from models import *

root = createTree([4,2,2,6,5,7,1,3])

def findFirst(root, Target):
    node = root
    result = None

    while node is not None:

        if node.getVal() == Target:
            result = node
            node = node.getRight()

        elif node.getVal() < Target:
            node = node.getRight()

        else:
            node = node.getLeft()

    return result

print(findFirst(root, 2).data)


