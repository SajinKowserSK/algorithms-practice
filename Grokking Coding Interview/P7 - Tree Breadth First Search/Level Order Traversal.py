from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  curr_lvl = []
  seen = set()
  q = []
  q.append(root)
  q.append(None)

  while len(q) > 0:
    popped = q.pop(0)

    # case where popped is None
    if popped is None:
      # we ran to the end of a level
      result.append(curr_lvl)
      curr_lvl = []
      q.append(None)

      if q[0] == None: # we just added None to the back so if front is same as back, nothing in between
        break

    else:

      # assuming popped is not None
      neighbors = [popped.left, popped.right]
      for neighbor in neighbors:
        if neighbor not in seen and neighbor is not None:
          q.append(neighbor)


      if popped not in seen:
        seen.add(popped)
        curr_lvl.append(popped.val)


  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
