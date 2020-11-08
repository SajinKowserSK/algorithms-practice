"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        adjList = {}

        adjList[node] = node.neighbors
        seen = set()
        seen.add(node)

        q = []
        q.append(node)

        while q:
            popped = q.pop(0)

            if popped not in seen:
                seen.add(popped)
                adjList[popped] = popped.neighbors

            for nbr in popped.neighbors:
                if nbr not in seen:
                    q.append(nbr)

        deep_adj = {}

        for key in adjList:
            deep_copy = Node(key.val, [])
            deep_adj[key.val] = deep_copy

        for key in adjList:
            deep_copy = deep_adj[key.val]

            for nbr in key.neighbors:
                deep_copy.neighbors.append(deep_adj[nbr.val])

        for key in deep_adj:
            return deep_adj[key]







