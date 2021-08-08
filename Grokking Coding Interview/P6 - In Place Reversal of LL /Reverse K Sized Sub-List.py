from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_every_k_elements(head, k):
    trav = 1
    prev = head
    curr = head

    lastTail = None

    while curr.next:
        curr = curr.next
        trav += 1

        if trav % k == 0:

            rest = curr.next
            curr.next = None

            # important to note that after reversing, "prev" actually becomes the tail
            # the head/start     is now reversed_head
            reversed_head = reverse(prev)

            if lastTail is not None:
                lastTail.next = reversed_head
                lastTail = prev

            else:
                lastTail = prev
                start = reversed_head

            prev = rest
            curr = rest
            trav = 1

    lastTail.next = reverse(prev)

    return start


def reverse(head):
    prev = None
    curr = head
    while curr:
        nextN = curr.next
        curr.next = prev
        prev = curr
        curr = nextN
    return prev


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()







