# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hmap = {}
        for e in range(len(inorder)):
            hmap[inorder[e]] = e 
            
            
        def helper(inorder, postorder):

            if len(inorder) == 0 or len(postorder) == 0:
                return None 

            root = TreeNode(postorder[-1])
            mid = inorder.index(root.val)
            
            # print(root.val, postorder, inorder)
            
            root.right = helper(inorder[mid+1::], postorder[mid:len(postorder)-1])
            root.left = helper(inorder[0:mid+1], postorder[0:mid])
            
            return root
        
        return helper(inorder, postorder)