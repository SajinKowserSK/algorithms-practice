from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  slow, fast = head, head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next


  h1 = head
  h2 = reverse(slow)

  while h1 and h2:
    tmp = h1.next
    h1.next = h2
    h1 = tmp

    tmp = h2.next
    h2.next = h1
    h2 = tmp

  h1.next = None

  return head

def reverse(head):
  curr = head
  prev = None

  while curr:
    next_n = curr.next
    curr.next = prev
    prev = curr
    curr = next_n

  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()
