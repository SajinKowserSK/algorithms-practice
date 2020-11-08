class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        adjList = {}
        for x in range(0, len(graph)):
            adjList[x] = graph[x]

        root = 0

        for key in adjList:
            if adjList[key] != []:
                root = key
                break

        bfs_arr = self.bfs_level(root, adjList)

        for level in bfs_arr:
            for node in level:
                for node2 in level:
                    if node in adjList[node2]:
                        return False

        return True

    def bfs_level(self, key, adj):
        master = []
        seen = set()

        q = []
        q.append(key)
        q.append(None)
        seen.add(key)

        curr = []
        curr.append(key)

        while q:
            popped = q.pop(0)

            if popped is None:
                master.append(curr)
                curr = []

                q.append(None)
                if q[0] is None:
                    break

                else:
                    continue

            if popped not in seen:
                seen.add(popped)
                curr.append(popped)

            for nbr in adj[popped]:
                if nbr not in seen:
                    q.append(nbr)

        return master