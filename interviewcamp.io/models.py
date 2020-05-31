# Binary Tree Node

class BinaryNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

    # def PrintTree(self):
    #     if self.left:
    #         self.left.PrintTree()
    #     print(self.data),
    #     if self.right:
    #         self.right.PrintTree()



