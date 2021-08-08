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


def reverse_alternate_k_elements(head, k):
  curr, prev, trav = head, head, 1

  lastTail, start = None, None

  while curr.next.next:
    curr = curr.next
    trav += 1
    div = trav / k

    if trav % k == 0 and div % 2 != 0:
      rest = curr.next
      curr.next = None

      rev_head = reverse(prev) # prev is now new tail, rev_head the new head

      if lastTail is None:
        lastTail = prev
        start = rev_head

      else:
        lastTail.next = rev_head
        lastTail = prev

      curr, prev = rest, rest
      trav += 1


    elif trav % k == 0 and div % 2 == 0:
      lastTail.next = prev
      lastTail = curr
      rest = curr.next


      curr, prev = rest, rest
      trav += 1

  trav += 1
  if trav % k == 0 and (trav / k) % 2 == 0:
    lastTail.next = prev

  else:
    lastTail.next = reverse(prev)

  return start




  return head

def reverse(head):
  curr, prev = head, None

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
  result = reverse_alternate_k_elements(head, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
