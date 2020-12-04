from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        # create adj list
        # do a dfs and check if the node is in a strongly connected component (SCC)
        # we check for SCC by tracking lowest_depth and curr_node_depth

        # both these values initialized to original depth level from starting node
        # however lowest_depth consistently updated to the lowest between
        # curr node and its neighbor

        # if for any node's nbr, we see that the node's lowest_depth
        # is actually less than our starting_depth then we know they're from diff SCC

        # NULL CHECKS
        adjList = defaultdict(list)
        adjList = self.create(connections, adjList)
        master = set()
        curr_node_depth = {}
        lowest_depth = {}
        criticals = []
        depth = 0

        self.dfs(adjList, 0, None, curr_node_depth, lowest_depth, depth, master)

        return list(master)

    def create(self, connections, adjList):

        for node1, node2 in connections:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        return adjList

    def dfs(self, adjList, curr, parent, curr_node_depth, lowest_depth, depth, master):
        curr_node_depth[curr] = depth
        lowest_depth[curr] = depth
        depth += 1  # for next iteration

        nbrs = adjList[curr]

        for nbr in nbrs:
            if nbr == parent:  # dont need to consider parent
                continue

            print(curr, nbr)
            if nbr in curr_node_depth:  # we've seen it before but we are processing again
                lowest_depth[curr] = min(lowest_depth[curr], lowest_depth[nbr])

            else:  # new node
                self.dfs(adjList, nbr, curr, curr_node_depth, lowest_depth, depth, master)

                lowest_depth[curr] = min(lowest_depth[curr], lowest_depth[nbr])

                if curr_node_depth[curr] < lowest_depth[nbr]:
                    # if the nbr was connected to any other
                    # component in the SCC, it would've had a lower lowest_depth and this condition
                    # wouldn't be met

                    print("curr stats", curr, curr_node_depth[curr], lowest_depth[curr])
                    print("nbr stats", nbr, curr_node_depth[nbr], lowest_depth[nbr])
                    min_v = min(curr, nbr)
                    max_v = max(curr, nbr)

                    entry = (min_v, max_v)
                    master.add(entry)





