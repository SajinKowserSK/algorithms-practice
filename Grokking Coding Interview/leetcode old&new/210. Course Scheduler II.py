class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:

        ## EDGE CASES for if arr is []

        adj = {}
        visited = {}

        children = {}

        for x in range(0, numCourses):
            adj[x] = []
            visited[x] = 0
            children[x] = []

        if len(prereqs) == 0:
            return list(children.keys())

        for pair in prereqs:
            course = pair[0]
            prereq_course = pair[1]

            adj[course].append(prereq_course)
            children[prereq_course].append(course)

        for key in adj:
            if self.dfs(key, adj, visited) == False:
                return []

        first = None
        for key in adj:
            if len(adj[key]) == 0:
                first = key

        if first is None:
            return []

        visited = dict.fromkeys(visited, False)

        output = []

        for key in visited:
            self.top_sort(key, children, visited, output)

        return output

    def dfs(self, key, adj, visited):
        if visited[key] == 1:
            return False

        visited[key] = 1

        for nbr in adj[key]:
            if visited[nbr] != 2 and self.dfs(nbr, adj, visited) == False:
                return False

        visited[key] = 2
        return True

    def top_sort(self, key, adj, visited, output):

        if visited[key] != True:

            visited[key] = True
            for nbr in adj[key]:
                self.top_sort(nbr, adj, visited, output)

            output.insert(0, key)


