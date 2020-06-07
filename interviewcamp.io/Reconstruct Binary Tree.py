# Medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    # driver
    def buildTree(self, preorder, inorder):
        inMap = self.inOrderMap(inorder)
        return self.construct(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inMap)

    # helper function to create a hashmap with each value and their position
    # in the inorder traversal
    # after finding root here, anything to left -> left subtree
    # anything to right -> right subtree

    def inOrderMap(self, inorderArr):
        myMap = {}
        for x in range(0, len(inorderArr)):
            myMap[inorderArr[x]] = x

        return myMap

    # helper function to construct each tree/subtree
    def construct(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        # base case for recursive function
        if preStart > preEnd or inStart > inEnd:
            return None

        rootNodeVal = preorder[preStart]
        rootNode = TreeNode(rootNodeVal)
        rootIndex = inMap[rootNodeVal]

        rootNode.left = self.construct(preorder, preStart + 1, preStart + (rootIndex - inStart), inorder, inStart,
                                       rootIndex - 1, inMap)

        rootNode.right = self.construct(preorder, preStart + (rootIndex - inStart) + 1, preEnd, inorder, rootIndex + 1,
                                        inEnd, inMap)

        return rootNode






