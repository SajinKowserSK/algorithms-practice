class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:

        if len(prereq) == 0:
            return True

        adj = {}

        for x in range(0, numCourses):
            adj[x] = []

        for pair in prereq:
            course = pair[0]
            prereq_course = pair[1]

            adj[course].append(prereq_course)

        visits = {}
        for key in adj:
            visits[key] = 0

        for key in adj:
            if not self.dfs(key, adj, visits):
                return False

        first = None
        for key in adj:
            if len(adj[key]) == 0:
                first = key
                break

        return False if first is None else True

    def dfs(self, key, adj, visits):
        if visits[key] == 1:
            return False

        visits[key] = 1
        for nbr in adj[key]:
            # if the neighbor is not done being visited and dfs is false
            if visits[nbr] != 2 and not self.dfs(nbr, adj, visits):
                return False

        visits[key] = 2
        return True


