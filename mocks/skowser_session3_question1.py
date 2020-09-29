class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    if head is None:
        return False

    slow = head
    fast = head

    while fast is not None:
        fast = fast.next
        if fast is None:
            break

        else:

            fast = fast.next

            if slow == fast:
                return True

            slow = slow.next


    return False

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

print(has_cycle(node1)) # False

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

print(has_cycle(node1)) # True
