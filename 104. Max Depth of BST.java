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
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(height(root.left), height(root.right))+1;
        
    }
    
    
    private int height (TreeNode root){
        if (root == null) return 0;
        
        else{
            
            int l_height = height(root.left);
            int r_height = height(root.right);
            
            if (l_height > r_height) return l_height + 1;
            else return r_height+1;
               
        }
    }
}