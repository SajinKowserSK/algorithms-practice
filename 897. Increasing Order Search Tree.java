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
    public TreeNode increasingBST(TreeNode root) {
        
        ArrayList <Integer> arr = new ArrayList <Integer>();
        arr = inOrderTraversal(root, arr);
        
//         TreeNode bst = new TreeNode(arr.get(0));
        
        TreeNode head = new TreeNode(arr.get(0));
        TreeNode bst = head;
        
        for (int x = 1; x < arr.size(); x++){
            head.left = null;
            head.right = new TreeNode(arr.get(x));
            head = head.right;
        }
        
        
        return bst;
        
    }
    
            
    private ArrayList<Integer> inOrderTraversal(TreeNode root, ArrayList<Integer> arr){
        if (root == null) return null;
        
        else{
            inOrderTraversal(root.left, arr);
            arr.add(root.val);
            inOrderTraversal(root.right, arr);
        }
        
        return arr;
        
    } 
    
    
    
    
}