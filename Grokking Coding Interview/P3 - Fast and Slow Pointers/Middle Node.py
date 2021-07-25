class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

''' alternatively could go '''
def find_middle_of_linked_list(head):
  slow, fast = head, head
  count = 0

  while fast != None:
      count += 1
      fast = fast.next

  mid_index = int(count/2)

  fast = head
  for x in range(mid_index):
      fast = fast.next

  while fast.next != None:
      slow = slow.next
      fast = fast.next




  return slow




def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()
