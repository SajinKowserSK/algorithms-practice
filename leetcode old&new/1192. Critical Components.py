class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adjList = {}
        for node1, node2 in connections:

            if node1 not in adjList:
                adjList[node1] = []

            if node2 not in adjList:
                adjList[node2] = []

            adjList[node1].append(node2)
            adjList[node2].append(node1)

        start = {}
        end = {}
        time = 0
        ans = set()
        visited = {}

        self.dfs(0, None, start, end, time, ans, visited, adjList)

        return list(ans)

    def dfs(self, key, parent, start, end, time, ans, visited, adjList):
        visited[key] = True
        start[key] = time
        end[key] = time

        time += 1

        nbrs = adjList[key]

        for nbr in nbrs:
            if nbr == parent:
                continue

            if nbr not in visited:
                self.dfs(nbr, key, start, end, time, ans, visited, adjList)

                end[key] = min(end[key], end[nbr])

                if start[key] < end[nbr]:
                    entry = (min(key, nbr), max(key, nbr))
                    ans.add(entry)

            else:
                end[key] = min(end[key], end[nbr])

