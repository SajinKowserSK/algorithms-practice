# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

            # creating master list and seen list (for bfs)
        master = []
        seen = set()

        # queue for bfs
        # adding root to the hash set

        q = []

        q.append(root)
        q.append(None)
        seen.add(root)
        curr_level = [root.val]

        while len(q) > 0:
            popped = q.pop(0)

            if popped == None:  # level finish

                # store whatever you need to for current level
                master.append(curr_level)
                curr_level = []

                # put in another null to signify the finish of child level
                q.append(None)

                # if finish of current level of None is followed by finish of child level of None, we are DONE

                if q[0] == None:
                    break

                else:
                    continue

            neighbors = [popped.left, popped.right]

            if popped not in seen:
                seen.add(popped)
                curr_level.append(popped.val)

            for neighbor in neighbors:
                if neighbor not in seen and neighbor is not None:
                    q.append(neighbor)

        return master





