# Binary Tree Node

class BinaryNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getVal(self):
        return self.data

    def isLeaf(self):
        return True if self.left is None and self.right is None else False

    # binary search type of insert
    def insertNode(self, data):

        if self.data == None:
            self.data = data

        else:
            if data > self.data:

                if self.right is None:
                    self.right = BinaryNode(data)

                else:
                    self.right.insertNode(data)

            elif data < self.data:

                if self.left is None:
                    self.left = BinaryNode(data)

                else:
                    self.left.insertNode(data)


def createTree(lst):
    root = BinaryNode(lst[0])
    for x in range (1, len(lst)):
        root.insertNode(lst[x])

    return root

def inOrder(root):
    if root is None:
        return None

    inOrder(root.left)
    print(root.data)
    inOrder(root.right)