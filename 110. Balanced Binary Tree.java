/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
                
        if (root == null) return true;
        
        else{
            
            if (isBalanced(root.left))

            
            if (Math.abs(height(root.left)-height(root.right)) > 1) return false;
            
            else{
                if (isBalanced(root.left)&&isBalanced(root.right)) return true;
            }
            
                return false;
        }
    }
    
    private int height (TreeNode root){
        if (root == null){            
            return 0;
        }
        
        else{
            
            int l_h = height(root.left);
            int r_h = height(root.right);
            
            if (l_h > r_h) return l_h + 1;
            else return r_h + 1;   
        }
    }
}