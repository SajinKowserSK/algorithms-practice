class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjList = {}
        visited = {}
        for x in range(len(graph)):
            adjList[x] = graph[x]
            visited[x] = False

        res = []
        cPath = []

        self.dfs(res, cPath, 0, adjList, visited, len(graph) - 1)

        return res

    def dfs(self, res, cPath, node, adjList, visited, target):
        print(cPath)
        if node == target:
            cPath.append(node)
            res.append(cPath.copy())

            visited[node] = False
            cPath.pop(-1)

        else:
            if visited[node] == False:
                visited[node] = True
                cPath.append(node)
                neighbors = adjList[node]

                for nbr in neighbors:
                    if visited[nbr] == False:
                        self.dfs(res, cPath, nbr, adjList, visited, target)

                visited[node] = False
                cPath.pop(-1)
