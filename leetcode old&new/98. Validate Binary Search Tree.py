# somewhat unordinary approach to this question
# using induction, we know for all BST, in order traversal will be a proper sorted array where arr[x+1] > arr[x]
# Medium level question, O(n) time, O(n) Space

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        inOrderArr = self.inOrder(root, [])
        
        bst = True 
        for x in range (0, len(inOrderArr)-1):
            if inOrderArr[x+1] <= inOrderArr[x]:
                bst = False 
                break 
        
        return bst 
        
    def inOrder(self, root, arr):
        if root is None:
            return arr 
        
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)
        
        return arr 
