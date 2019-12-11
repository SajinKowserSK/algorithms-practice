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
    public int sumOfLeftLeaves(TreeNode root) {
    
        int retVal = 0;
        if (root == null) return retVal;
        
        retVal += leftMost(root.left);
        
        // traverses right subtree 
        if (root.right != null){
            
            // doesn't traverse if there is no right subtree and only right child 
            if (isLeaf(root.right) == false){
                retVal += leftMost(root.right);
            }
        }
        return retVal;
    }
    
    private int leftMost (TreeNode root){
        
        // base case
        if (isLeaf(root)) return root.val;
        
        // recursive case 
        else{
            int retVal = 0;
            if (root != null){
                retVal += leftMost(root.left);
                if (root.right != null){
                    if (isLeaf(root.right) == false){
                        retVal += leftMost(root.right);
                    }
                }
            } 
            return retVal;
        }
    }
    
    private boolean isLeaf (TreeNode root){
        if (root != null && root.left == null && root.right == null) return true;
        else return false;
    }
}