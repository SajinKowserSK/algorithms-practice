# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        len1, len2 = 0, 0
        curr1, curr2 = l1, l2
        while curr1:
            len1 += 1 
            curr1 = curr1.next
        while curr2:
            len2 += 1 
            curr2 = curr2.next
            
        curr1, curr2 = l1, l2 
        
        if len1 > len2:
            ret = self.helper(curr1, curr2)
            
        else:
            ret = self.helper(curr2, curr1)
            
        return ret 
        
    def helper(self, curr1, curr2):
        head = curr1 
        prev = None 

        carry = 0 
        while curr2:
            prev = curr1
            curr1.val += int(carry)  #Mutate only bigger one bc we gonna connect the rest
            currSum = curr1.val + curr2.val

            currSum = str(currSum)

            if len(currSum) > 1:
                carry = currSum[0]

            else:
                carry = 0 

            currSum = currSum[-1]

            curr1.val = currSum

            curr1 = curr1.next
            curr2 = curr2.next

        # curr2 ends 
        if curr1 is not None:

            while curr1.next:

                summed = curr1.val + int(carry)
                carry = 0 
                summed = str(summed)

                if len(summed) > 1:
                    curr1.val = int(summed[1])
                    carry = int(summed[0])

                else:
                    print(curr1.val, summed)
                    curr1.val = int(summed)

                curr1 = curr1.next

            if curr1.next is None and carry != 0:
                summed = int(curr1.val) + int(carry)
                carry = 0 

                if len(str(summed)) > 1:
                    curr1.val = int(str(summed)[1])
                    carry = int(str(summed)[0])

                    curr1.next = ListNode(carry)

                else:
                    curr1.val = summed
                    
        else:
            if carry != 0: 
                prev.next = ListNode(carry)
                

            
        
        return head
            
            
        