from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  slow, fast = head, head

  while fast is not None and fast.next is not None:
      fast = fast.next.next
      slow = slow.next

      if fast == slow:
          cycleLen = calculateCycle(slow)
          break
          # calculate length of cycle

  slow, fast = head, head

  while cycleLen > 0:
      fast = fast.next
      cycleLen -= 1

  while fast != slow:
      fast = fast.next
      slow = slow.next

  return slow


def calculateCycle(slow):
    fast = slow.next
    cycleLen = 1

    while fast != slow:
        fast = fast.next
        cycleLen += 1

    return cycleLen

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
