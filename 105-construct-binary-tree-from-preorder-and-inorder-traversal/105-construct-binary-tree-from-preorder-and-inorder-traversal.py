# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None 
        
        # pre order processes root first, so start of the arr will be the root 
        # in order does left -> root -> right so the inorder mid will be the root 
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        # we know where the root is in order
        # for the left subtree we will need 1:mid (inclusive) nodes because that's how many are left of the root 
        # for the right subtree we will need mid+1 to end nodes because thats how many are right to the root
        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right= self.buildTree(preorder[mid+1::], inorder[mid+1::])
        
        return root 