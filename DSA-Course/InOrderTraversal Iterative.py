# given a binary tree, return a list of it's inorder traversal result

from models import BinaryNode

givenTree = BinaryNode(4)
givenTree.insertNode(2)
givenTree.insertNode(6)
givenTree.insertNode(1)
givenTree.insertNode(3)
givenTree.insertNode(5)
givenTree.insertNode(7)

def iterativeInOrder(root):
    if root is None:
        return []

    retList = []
    stk = []
    curr = root
    while curr is not None or len(stk) > 0:
        if curr is not None:
            stk.insert(0, curr.getVal())
            curr = curr.getLeft()

        else:
            front = stk[0]
            retList.append(front)
            stk.remove(front)
            curr = curr.getRight()

    return retList


print(iterativeInOrder(givenTree))
