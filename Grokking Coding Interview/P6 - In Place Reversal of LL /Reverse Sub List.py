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


def reverse_sub_list(head, p, q):
    iterations = q - p + 1
    curr, prev = head, None

    traversed = 1
    while traversed < p:
        prev = curr
        curr = curr.next
        traversed += 1

        # curr is now at p

    q_ptr = curr

    while traversed < q:
        q_ptr = q_ptr.next
        traversed += 1

    rest = q_ptr.next  # copy the rest
    q_ptr.next = None

    rest.print_list()

    prev.next = reverse(curr)

    tail = prev
    while tail.next:
        tail = tail.next

    tail.next = rest

    return prev


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

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
