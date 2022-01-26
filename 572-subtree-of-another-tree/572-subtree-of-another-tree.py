# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None: 
            return None 
        
        else:
            if root.val == subRoot.val:
                if self.helper(root, subRoot): 
                    return True 
            
            return True if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) else False 
        
    def helper(self, root, subRoot):
        rList = [] 
        sList = []
        self.trav(root, rList)
        self.trav(subRoot, sList)
        
        if len(rList) != len(sList):
            return False 
        
        for x in range(0, len(rList)):
            if rList[x] != sList[x]:
                return False 
            
        return True 
    
    def trav(self, root, lst):
        if root is not None:
            self.trav(root.left, lst)
            lst.append(root.val)
            self.trav(root.right, lst)
            
            
        