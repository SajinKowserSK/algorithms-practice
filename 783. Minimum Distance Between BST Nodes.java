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
    public int minDiffInBST(TreeNode root) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr = inOrderTraversal(root, arr);
        System.out.println(arr);
        // return arr.get(1)-arr.get(0);
        int lowest = arr.get(1) - arr.get(0);
        for (int i = 1; i < arr.size()-1; i++){
            if (arr.get(i+1)-arr.get(i) < lowest)
                lowest = arr.get(i+1)-arr.get(i);
           
        }
       
        return lowest;
    }
   
    public static ArrayList<Integer> inOrderTraversal(TreeNode root, ArrayList<Integer> arr){
        if (root == null) return null;
       
        else{
            inOrderTraversal(root.left, arr);
            arr.add(root.val);
            inOrderTraversal(root.right, arr);
        }
       
        return arr;
       
    }
}