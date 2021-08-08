/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }

> get array list sorted min to largest with inorder traversal
> for x in list, get sum (inclusive) and put htat in int sum var
> do a search() function and replace the value with sum
 */
class Solution {
    public TreeNode bstToGst(TreeNode root) {
        ArrayList <Integer> arr = new ArrayList <Integer>();
        arr = inOrderTraversal(root, arr);
       
        
        for (int i = 0; i < arr.size(); i++){
            int sum = arr.get(i);
            for (int j = i+1; j < arr.size(); j++){
                sum += arr.get(j);
            }
            
            search(root, arr.get(i), sum);
        }
      
        return root;
        
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
    
    public void search(TreeNode root, int val, int newVal) { 
    // Base Cases: root is null or key is present at root 
    if (root != null){
         if (root.val == val) root.val = newVal; 
  
        else if (root.val > val) search(root.left, val, newVal); 

        search(root.right, val, newVal); 
        
    }
   
    } 
}