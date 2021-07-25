class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  slow, fast = head, head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  # slow is now mid_index
  secondHalf = reverse(slow)
  copy_secondHalf = secondHalf # to be reversed later

  headPtr = head
  secPtr = secondHalf

  while headPtr is not None and secPtr is not None:
    if headPtr.value != secPtr.value:
      return False

    headPtr = headPtr.next
    secPtr = secPtr.next

  reverse(copy_secondHalf)
  return True


def reverse(head):
  curr = head
  prev = None

  while curr is not None:
     next_node = curr.next
     curr.next = prev
     prev = curr
     curr = next_node

  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()







