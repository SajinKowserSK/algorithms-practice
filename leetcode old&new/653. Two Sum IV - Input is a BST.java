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
    public boolean findTarget(TreeNode root, int k) {
        
        ArrayList<Integer> arr = new ArrayList<Integer>();
        inOrderTraversal(root, arr);
        System.out.println(arr);
        
        for (int x = 0; x < arr.size(); x++){
            for (int y = x+1; y < arr.size(); y++){
                if (arr.get(x) + arr.get(y) == k){
                    return true;
                }
            }
        }
        
        return false;
        
        
    }
    
    
    // helper method to get values in increasing order
    public ArrayList<Integer> inOrderTraversal(TreeNode root, ArrayList<Integer> arr){
        if (root == null) return null;
        
        else{
            inOrderTraversal(root.left, arr);
            arr.add(root.val);
            inOrderTraversal(root.right, arr);
        }
        
        return arr;
        
    }
}