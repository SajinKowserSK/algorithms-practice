/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        
        int counter = 0;
        ListNode temp = head;
        
        // iterate through linkedlist and get size
        while (temp != null){
            counter++;
            temp = temp.next;
        }
        
        // mid 
        int mid = counter / 2;
        
        // iterate until mid node and return mid node
        counter = 0;
        while (counter < mid){
            head = head.next;
            counter++;
        }
        
        return head;
            
        
    }
}